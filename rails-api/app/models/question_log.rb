class QuestionLog < ApplicationRecord
    belongs_to :store
  
    validates :question, presence: true
    validates :response, presence: true
  end
  