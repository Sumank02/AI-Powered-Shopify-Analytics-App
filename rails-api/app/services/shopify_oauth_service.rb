class ShopifyOauthService
    def initialize(shop_name:, code:)
      @shop_name = shop_name
      @code = code
    end
  
    def exchange_token
      uri = URI("https://#{@shop_name}/admin/oauth/access_token")
      res = Net::HTTP.post_form(uri, {
        client_id: ENV["SHOPIFY_API_KEY"],
        client_secret: ENV["SHOPIFY_API_SECRET"],
        code: @code
      })
      JSON.parse(res.body)
    end
  
    def save_token(store)
      token_data = exchange_token
      store.create_shopify_token!(access_token: token_data["access_token"])
    end
  end
  