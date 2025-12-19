require_relative "boot"

require "rails"
require "active_model/railtie"
require "active_record/railtie"
require "action_controller/railtie"
require "action_view/railtie"

Bundler.require(*Rails.groups)

module AiShopifyAnalytics
  class Application < Rails::Application
    config.load_defaults 7.1
    
    # Enable session middleware for OAuth (needed for CSRF token)
    config.middleware.use ActionDispatch::Cookies
    config.middleware.use ActionDispatch::Session::CookieStore, key: '_ai_shopify_session'
    
    # Enable serving static files and views for frontend
    config.public_file_server.enabled = true
  end
end
