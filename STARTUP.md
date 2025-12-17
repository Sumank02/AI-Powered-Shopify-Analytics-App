# Startup Guide - AI-Powered Shopify Analytics App

## Prerequisites

- **Ruby 3.2.2+** and Rails 7.1+
- **Python 3.11+**
- **PostgreSQL** (or use Docker)
- **Docker & Docker Compose** (optional, for containerized setup)

---

## Option 1: Manual Setup (Development)

### Step 1: Setup Environment Variables

Create a `.env` file in the root directory:

```bash
# Copy from example (if .env.example exists)
cp .env.example .env
```

Or create `.env` manually with:

```env
# Rails API
RAILS_ENV=development
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_NAME=ai_shopify_db_development

# Shopify OAuth
SHOPIFY_API_KEY=your_shopify_api_key
SHOPIFY_API_SECRET=your_shopify_api_secret
SHOPIFY_REDIRECT_URI=http://localhost:3000/api/v1/shopify/callback

# Python AI Service
PYTHON_AI_SERVICE_URL=http://localhost:8000/api/v1/questions

# Optional: LLM Provider
OPENAI_API_KEY=your_openai_api_key
```

### Step 2: Setup PostgreSQL Database

**Windows:**
```powershell
# Install PostgreSQL or use Docker
docker run -d --name postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=ai_shopify_db_development -p 5432:5432 postgres:15
```

**Mac/Linux:**
```bash
# Using Docker
docker run -d --name postgres -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=ai_shopify_db_development -p 5432:5432 postgres:15

# Or install PostgreSQL locally and create database
createdb ai_shopify_db_development
```

### Step 3: Setup Rails API

```bash
cd rails-api

# Install Ruby dependencies
bundle install

# Setup database
rails db:create
rails db:migrate

# Start Rails server (in one terminal)
rails server -p 3000
```

### Step 4: Setup Python AI Service

**Open a new terminal:**

```bash
cd python-ai-service

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
.\venv\Scripts\activate.bat
# Mac/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn app.main:app --reload --port 8000
```

### Step 5: Verify Services

- **Rails API:** http://localhost:3000/health
- **Python AI Service:** http://localhost:8000/health

---

## Option 2: Docker Compose Setup (Recommended)

### Step 1: Create .env file

Create `.env` in the root directory:

```env
RAILS_ENV=development
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_HOST=db
DATABASE_NAME=ai_shopify_db

SHOPIFY_API_KEY=your_shopify_api_key
SHOPIFY_API_SECRET=your_shopify_api_secret
SHOPIFY_REDIRECT_URI=http://localhost:3000/api/v1/shopify/callback

PYTHON_AI_SERVICE_URL=http://python-ai-service:8000/api/v1/questions

OPENAI_API_KEY=your_openai_api_key
```

### Step 2: Build and Start Services

```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

### Step 3: Setup Rails Database (First Time)

```bash
# In a new terminal, run migrations
docker-compose exec rails-api rails db:create db:migrate
```

### Step 4: Verify Services

- **Rails API:** http://localhost:3000/health
- **Python AI Service:** http://localhost:8000/health
- **PostgreSQL:** localhost:5432

---

## Testing the API

### Test Python AI Service Directly

```bash
curl -X POST http://localhost:8000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d '{
    "store_id": "example-store.myshopify.com",
    "question": "What are my top selling products?"
  }'
```

### Test Rails API (which forwards to Python)

```bash
curl -X POST http://localhost:3000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d '{
    "store_id": "example-store.myshopify.com",
    "question": "How much inventory should I reorder for next week?"
  }'
```

### Expected Response

```json
{
  "answer": "Your top selling products are: Product A (300 units sold), Product B (220 units sold).",
  "confidence": "high",
  "metadata": {
    "intent": "sales",
    "plan": {
      "resource": "orders",
      "metrics": ["total_quantity", "total_sales"],
      "time_window": {
        "start_date": "2024-11-17",
        "end_date": "2024-12-17"
      }
    },
    "shopifyql": "FROM orders SHOW sum(line_items.quantity) AS total_quantity, sum(total_price) AS total_sales GROUP BY line_items.product_title SINCE 2024-11-17 UNTIL 2024-12-17 ORDER BY total_quantity DESC LIMIT 5"
  }
}
```

---

## Troubleshooting

### Rails Issues

**Database connection error:**
- Ensure PostgreSQL is running
- Check `.env` file has correct database credentials
- Verify `DATABASE_HOST` matches your setup (localhost for manual, `db` for Docker)

**Bundle install fails:**
- Ensure Ruby 3.2.2+ is installed: `ruby -v`
- Try: `bundle update`

**Port 3000 already in use:**
- Change port: `rails server -p 3001`
- Or kill process using port 3000

### Python Issues

**Module not found errors:**
- Ensure virtual environment is activated
- Reinstall: `pip install -r requirements.txt`

**Port 8000 already in use:**
- Change port: `uvicorn app.main:app --reload --port 8001`
- Update `PYTHON_AI_SERVICE_URL` in `.env`

**Import errors:**
- Ensure you're running from `python-ai-service` directory
- Check all `__init__.py` files exist in package directories

### Docker Issues

**Build fails:**
- Check Docker is running: `docker ps`
- Try: `docker-compose down` then `docker-compose up --build`

**Database connection:**
- Wait for PostgreSQL to fully start (may take 10-20 seconds)
- Check logs: `docker-compose logs db`

---

## Development Workflow

1. **Make code changes** in `rails-api/` or `python-ai-service/`
2. **Rails** auto-reloads (if using `rails server`)
3. **Python** auto-reloads (if using `--reload` flag)
4. **Test endpoints** using curl or Postman
5. **Check logs** in terminal or `docker-compose logs`

---

## Stopping Services

### Manual Setup
- Press `Ctrl+C` in each terminal

### Docker Compose
```bash
docker-compose down
```

---

## Next Steps

- Configure Shopify OAuth credentials
- Set up real LLM provider (OpenAI/Claude/Gemini)
- Implement real Shopify API integration
- Add authentication middleware
- Set up logging and monitoring

