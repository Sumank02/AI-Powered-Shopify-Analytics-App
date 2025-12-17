class ResponseFormatter
    def self.format(ai_response)
      {
        answer: ai_response["answer"] || "",
        confidence: ai_response["confidence"] || "medium",
        metadata: ai_response["metadata"] || {}
      }
    end
  end
  