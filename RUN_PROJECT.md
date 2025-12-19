# 🚀 Commands to Run the Project

## Quick Start (Both Services)

You need **2 terminal windows** - one for Rails API, one for Python AI Service.

---

## Terminal 1: Python AI Service

**Open PowerShell and run:**

```powershell
cd D:\AI-Powered-Shopify-Analytics-App\python-ai-service
python -m uvicorn app.main:app --reload --port 8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Keep this terminal open!**

---

## Terminal 2: Rails API

**Open a NEW PowerShell window and run:**

```powershell
cd D:\AI-Powered-Shopify-Analytics-App\rails-api
bundle exec rails server -p 3000
```

**Expected output:**
```
=> Booting Puma
=> Rails 7.1.6 application starting in development
* Listening on http://127.0.0.1:3000
```

**Keep this terminal open!**

---

## ✅ Verify Services Are Running

### Check Python Service:
Open browser: **http://localhost:8000/health**

Should see:
```json
{
  "status": "ok",
  "service": "python-ai-service",
  "message": "AI service is running"
}
```

### Check Rails API:
Open browser: **http://localhost:3000/health**

Should see:
```
Rails API is running
```

### Check Frontend Application:
Open browser: **http://localhost:3000/**

Should see the **full web application UI** with:
- Connect Shopify Store section
- Ask Questions form
- Example questions buttons

---

## 🧪 Test the Full Application

### Option 1: Use the Web UI (Easiest)
1. Go to: **http://localhost:3000/**
2. Enter store name: `example-store.myshopify.com`
3. Click "Connect Store" (or skip if just testing)
4. Enter a question: `What are my top selling products?`
5. Click "Get Answer"
6. See the result!

### Option 2: Test via API (PowerShell)

**Test Python service directly:**
```powershell
$body = @{
    store_id = "example-store.myshopify.com"
    question = "What are my top selling products?"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/questions" -Method POST -ContentType "application/json" -Body $body
```

**Test Rails API (forwards to Python):**
```powershell
$body = @{
    store_id = "example-store.myshopify.com"
    question = "How much inventory should I reorder for next week?"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:3000/api/v1/questions" -Method POST -ContentType "application/json" -Body $body
```

---

## 📋 Complete Command Sequence

### First Time Setup (One-time only):

```powershell
# 1. Install Python dependencies
cd D:\AI-Powered-Shopify-Analytics-App\python-ai-service
pip install -r requirements.txt

# 2. Install Ruby gems
cd D:\AI-Powered-Shopify-Analytics-App\rails-api
bundle install

# 3. Setup database
bundle exec rails db:create
bundle exec rails db:migrate
```

### Every Time You Run the Project:

**Terminal 1 (Python):**
```powershell
cd D:\AI-Powered-Shopify-Analytics-App\python-ai-service
python -m uvicorn app.main:app --reload --port 8000
```

**Terminal 2 (Rails):**
```powershell
cd D:\AI-Powered-Shopify-Analytics-App\rails-api
bundle exec rails server -p 3000
```

---

## 🛑 Stopping the Services

- **Python Service:** Press `Ctrl+C` in Terminal 1
- **Rails API:** Press `Ctrl+C` in Terminal 2

---

## 🔧 Troubleshooting

### Python service won't start:
- Check if port 8000 is already in use
- Try: `python -m uvicorn app.main:app --reload --port 8001`
- Update `.env` if you change the port

### Rails won't start:
- Check if port 3000 is already in use
- Try: `bundle exec rails server -p 3001`
- Make sure database is created: `bundle exec rails db:create`

### Frontend not loading:
- Make sure Rails is running on port 3000
- Check browser console for errors
- Try: `http://localhost:3000/` (root path)

---

## 📍 URLs Summary

| Service | URL | Purpose |
|---------|-----|---------|
| **Frontend App** | http://localhost:3000/ | Main web application |
| **Rails Health** | http://localhost:3000/health | Rails API status |
| **Python Health** | http://localhost:8000/health | Python service status |
| **Python Docs** | http://localhost:8000/docs | API documentation (Swagger) |
| **Rails API** | http://localhost:3000/api/v1/questions | POST questions here |

---

## ✅ Success Checklist

- [ ] Python service running (Terminal 1 shows "Application startup complete")
- [ ] Rails API running (Terminal 2 shows "Listening on http://127.0.0.1:3000")
- [ ] http://localhost:8000/health returns JSON
- [ ] http://localhost:3000/health returns "Rails API is running"
- [ ] http://localhost:3000/ shows the web application UI
- [ ] Can ask questions and get answers!

---

**🎉 Once both services are running, you have a fully functional AI-powered Shopify Analytics application!**

