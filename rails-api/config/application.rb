require_relative "boot"

require "rails"
require "active_model/railtie"
require "active_record/railtie"
require "action_controller/railtie"

Bundler.require(*Rails.groups)

module AiShopifyAnalytics
  class Application < Rails::Application
    config.load_defaults 7.1
    config.api_only = true
    
    # Enable session middleware for OAuth (needed for CSRF token)
    config.middleware.use ActionDispatch::Cookies
    config.middleware.use ActionDispatch::Session::CookieStore, key: '_ai_shopify_session'
  end
end
