Rails.application.routes.draw do
    # Frontend Application
    root to: "home#index"
    get "/app", to: "home#index"
  
    namespace :api do
      namespace :v1 do
  
        # Shopify OAuth
        get  "/shopify/auth",     to: "shopify_auth#auth"
        get  "/shopify/callback", to: "shopify_auth#callback"
  
        # Analytics Questions
        post "/questions", to: "questions#create"
  
      end
    end
  
    # Health check
    get "/health", to: proc { [200, {}, ["Rails API is running"]] }
  end
  