class CreateQuestionLogs < ActiveRecord::Migration[7.1]
  def change
    create_table :question_logs do |t|
      t.references :store, null: false, foreign_key: true
      t.text :question, null: false
      t.text :response, null: false
      t.string :confidence
      t.json :metadata

      t.timestamps
    end
  end
end

