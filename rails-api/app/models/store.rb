class Store < ApplicationRecord
    has_one :shopify_token, dependent: :destroy
    has_many :question_logs, dependent: :destroy
  
    validates :shop_name, presence: true, uniqueness: true
    validates :domain, presence: true, uniqueness: true
  end
  