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

        response = forward_to_python_ai(store_id, question)

        render json: response
      rescue KeyError => e
        render json: { error: "Missing parameter", details: e.message }, status: 400
      end

      private

      def forward_to_python_ai(store_id, question)
        uri = URI(PYTHON_AI_SERVICE_URL)

        http = Net::HTTP.new(uri.host, uri.port)
        http.read_timeout = 10

        req = Net::HTTP::Post.new(uri.path, { "Content-Type" => "application/json" })
        req.body = { store_id: store_id, question: question }.to_json

        res = http.request(req)
        JSON.parse(res.body)
      rescue StandardError => e
        { error: "Failed to connect to AI service", details: e.message }
      end

    end
  end
end
