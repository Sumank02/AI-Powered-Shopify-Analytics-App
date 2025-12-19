require 'net/http'
require 'json'
require 'uri'

class PythonAiService
  PYTHON_AI_SERVICE_URL = ENV.fetch("PYTHON_AI_SERVICE_URL", "http://localhost:8000/api/v1/questions")

  def initialize(store_id:, question:, access_token: nil)
    @store_id = store_id
    @question = question
    @access_token = access_token
  end

  def call
    uri = URI(PYTHON_AI_SERVICE_URL)

    http = Net::HTTP.new(uri.host, uri.port)
    http.read_timeout = 30

    request = Net::HTTP::Post.new(uri.path, { "Content-Type" => "application/json" })
    
    # Include access_token if available (from Shopify OAuth)
    body = { 
      store_id: @store_id, 
      question: @question 
    }
    body[:access_token] = @access_token if @access_token.present?
    
    request.body = body.to_json

    response = http.request(request)
    JSON.parse(response.body)
  rescue StandardError => e
    { "error" => "Failed to connect to AI service", "details" => e.message }
  end
end
