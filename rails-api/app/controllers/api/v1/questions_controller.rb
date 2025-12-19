require 'net/http'
require 'json'
require 'uri'

module Api
  module V1
    class QuestionsController < BaseController

      PYTHON_AI_SERVICE_URL = ENV.fetch("PYTHON_AI_SERVICE_URL", "http://localhost:8000/api/v1/questions")

      def create
        store_id = params.require(:store_id)
        question = params.require(:question)
        access_token = params[:access_token] # Optional - get from store's token if available

        # Try to get access token from database if not provided
        # Gracefully handle if store doesn't exist (demo mode)
        if access_token.blank? && defined?(Store)
          begin
            store = Store.find_by(domain: store_id) || Store.find_by(shop_name: store_id)
            access_token = store&.shopify_token&.access_token if store
          rescue => e
            # If database lookup fails, continue without token (demo mode)
            Rails.logger.warn("Store lookup failed: #{e.message}")
            access_token = nil
          end
        end

        response = forward_to_python_ai(store_id, question, access_token)

        render json: response
      rescue KeyError => e
        render json: { error: "Missing parameter", details: e.message }, status: 400
      rescue => e
        Rails.logger.error("QuestionsController error: #{e.class.name}: #{e.message}")
        Rails.logger.error(e.backtrace.join("\n")) if e.backtrace
        render json: { error: "Internal Server Error", details: e.message }, status: 500
      end

      private

      def forward_to_python_ai(store_id, question, access_token = nil)
        uri = URI(PYTHON_AI_SERVICE_URL)

        http = Net::HTTP.new(uri.host, uri.port)
        http.read_timeout = 30

        req = Net::HTTP::Post.new(uri.path, { "Content-Type" => "application/json" })
        
        body = { store_id: store_id, question: question }
        body[:access_token] = access_token if access_token.present?
        
        req.body = body.to_json

        res = http.request(req)
        JSON.parse(res.body)
      rescue StandardError => e
        { error: "Failed to connect to AI service", details: e.message }
      end

    end
  end
end
