__AI-Powered Shopify Analytics App__

📌 Overview

An AI-powered analytics application built using Ruby on Rails and Python that connects to a Shopify store and answers natural-language business questions.
The system reads sales, inventory, and customer data from Shopify, converts user questions into ShopifyQL, and returns simple, human-friendly insights with confidence scores.

This project demonstrates how to combine backend APIs, LLM-based agents, and Shopify analytics in a clean, production-ready architecture.

📂 Project Structure
```
ai-shopify-analytics/
├── rails-api/                 # Rails API (OAuth, request handling)
├── python-ai-service/         # AI agent + ShopifyQL execution
├── docker-compose.yml         # Optional container setup
├── .env.example               # Environment variable template
└── README.md                  # Project documentation (this file)
```


🛠️ Requirements & Setup

To run this project locally, you need:

- Ruby 3.x + Rails (API-only)
- Python 3.10+
- PostgreSQL
- Shopify Partner account (for real data)
- OpenAI / LLM API key (optional – mock supported)

Basic setup:
```
# Rails API
cd rails-api
bundle install
rails db:create db:migrate
rails s
```
```
# Python AI Service
cd python-ai-service
pip install -r requirements.txt
uvicorn app.main:app --reload
```


🤖 What the Application Does

The system supports questions like:

- “What were my top 5 selling products last week?”
- “How much inventory should I reorder for next week?”
- “Which products may go out of stock soon?”
- “Which customers placed repeat orders in the last 90 days?”

Behind the scenes, the AI service:

- Classifies user intent (sales / inventory / customers)
- Plans required metrics and time range
- Generates valid ShopifyQL queries
- Executes queries using Shopify Admin API
- Converts raw data into clear business explanations

📊 Sample API Interaction

Request
```
{
  "store_id": "example-store.myshopify.com",
  "question": "How much inventory should I reorder for next week?"
}
```


Response
```
{
  "answer": "Based on recent sales, you should reorder around 70 units to avoid stockouts next week.",
  "confidence": "medium"
}
```

✅ When This Project is Useful

This project is useful for:

- Learning how to build AI-powered analytics applications
- Understanding Shopify OAuth + ShopifyQL analytics
- Demonstrating agent-based LLM workflows
- Showcasing clean Rails + Python microservice architecture
- Interview or portfolio projects involving AI + real-world APIs

The architecture can easily be extended to other e-commerce or analytics use cases.