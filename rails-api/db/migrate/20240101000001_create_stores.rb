class CreateStores < ActiveRecord::Migration[7.1]
  def change
    create_table :stores do |t|
      t.string :shop_name, null: false
      t.string :domain, null: false

      t.timestamps
    end

    add_index :stores, :shop_name, unique: true
    add_index :stores, :domain, unique: true
  end
end

