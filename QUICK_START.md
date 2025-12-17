# Quick Start Commands

## 🚀 Fastest Way: Docker Compose

```bash
# 1. Create .env file (copy template below)
# 2. Start all services
docker-compose up --build

# 3. In another terminal, setup database
docker-compose exec rails-api rails db:create db:migrate

# 4. Test endpoints
curl http://localhost:3000/health
curl http://localhost:8000/health
```

---

## 📝 Manual Setup

### Terminal 1: PostgreSQL
```bash
docker run -d --name postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=ai_shopify_db_development -p 5432:5432 postgres:15
```

### Terminal 2: Rails API
```bash
cd rails-api
bundle install
rails db:create db:migrate
rails server -p 3000
```

### Terminal 3: Python AI Service
```bash
cd python-ai-service
python -m venv venv

# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

---

## 🧪 Test the API

```bash
# Test Python service directly
curl -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d "{\"store_id\": \"example-store.myshopify.com\", \"question\": \"What are my top selling products?\"}"

# Test Rails API (forwards to Python)
curl -X POST http://localhost:3000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d "{\"store_id\": \"example-store.myshopify.com\", \"question\": \"How much inventory should I reorder?\"}"
```

---

## 📋 .env File Template

Create `.env` in root directory:

```env
RAILS_ENV=development
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
SHOPIFY_API_KEY=your_key
SHOPIFY_API_SECRET=your_secret
SHOPIFY_REDIRECT_URI=http://localhost:3000/api/v1/shopify/callback
PYTHON_AI_SERVICE_URL=http://localhost:8000/api/v1/questions
```

For Docker, use `DATABASE_HOST=db` instead of `localhost`.

