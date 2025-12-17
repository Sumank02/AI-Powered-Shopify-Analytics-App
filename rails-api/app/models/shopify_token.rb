class ShopifyToken < ApplicationRecord
    belongs_to :store
  
    validates :access_token, presence: true
  end
  