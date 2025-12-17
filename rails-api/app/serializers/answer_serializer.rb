class AnswerSerializer
    include JSONAPI::Serializer
  
    attributes :answer, :confidence, :metadata
  
    def metadata
      object[:metadata] || {}
    end
  end
  