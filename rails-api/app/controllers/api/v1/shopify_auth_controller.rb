require 'net/http'
require 'json'
require 'uri'
require 'securerandom'

module Api
    module V1
      class ShopifyAuthController < BaseController
        SHOPIFY_API_KEY = ENV["SHOPIFY_API_KEY"]
        SHOPIFY_API_SECRET = ENV["SHOPIFY_API_SECRET"]
        SCOPES = "read_orders,read_products,read_inventory"
        REDIRECT_URI = ENV.fetch("SHOPIFY_REDIRECT_URI", "http://localhost:3000/api/v1/shopify/callback")
  
        def auth
          shop = params[:shop]
          if shop.blank?
            render json: { error: "Missing shop parameter" }, status: 400 and return
          end
  
          install_url = "https://#{shop}/admin/oauth/authorize?client_id=#{SHOPIFY_API_KEY}&scope=#{SCOPES}&redirect_uri=#{REDIRECT_URI}&state=#{csrf_token}&grant_options[]=per-user"
  
          redirect_to install_url
        end
  
        def callback
          shop = params[:shop]
          code = params[:code]
  
          if shop.blank? || code.blank?
            render json: { error: "Missing parameters in callback" }, status: 400 and return
          end
  
          token_response = request_access_token(shop, code)
          # In production, save token securely in DB
          render json: { store: shop, access_token: token_response["access_token"] }
        rescue StandardError => e
          render json: { error: "OAuth failed", details: e.message }, status: 500
        end
  
        private
  
        def csrf_token
          session[:csrf_token] ||= SecureRandom.hex(16)
        end
  
        def request_access_token(shop, code)
          uri = URI("https://#{shop}/admin/oauth/access_token")
  
          res = Net::HTTP.post_form(uri, {
            client_id: SHOPIFY_API_KEY,
            client_secret: SHOPIFY_API_SECRET,
            code: code
          })
  
          JSON.parse(res.body)
        end
      end
    end
  end
  