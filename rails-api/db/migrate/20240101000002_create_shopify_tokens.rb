class CreateShopifyTokens < ActiveRecord::Migration[7.1]
  def change
    create_table :shopify_tokens do |t|
      t.references :store, null: false, foreign_key: true
      t.text :access_token, null: false

      t.timestamps
    end
  end
end

