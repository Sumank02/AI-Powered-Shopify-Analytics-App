require 'net/http'
require 'json'
require 'uri'

class PythonAiService
  PYTHON_AI_SERVICE_URL = ENV.fetch("PYTHON_AI_SERVICE_URL", "http://localhost:8000/api/v1/questions")

  def initialize(store_id:, question:)
    @store_id = store_id
    @question = question
  end

  def call
    uri = URI(PYTHON_AI_SERVICE_URL)

    http = Net::HTTP.new(uri.host, uri.port)
    http.read_timeout = 10

    request = Net::HTTP::Post.new(uri.path, { "Content-Type" => "application/json" })
    request.body = { store_id: @store_id, question: @question }.to_json

    response = http.request(request)
    JSON.parse(response.body)
  rescue StandardError => e
    { "error" => "Failed to connect to AI service", "details" => e.message }
  end
end
