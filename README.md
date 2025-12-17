# AI‑Powered Shopify Analytics App

## Overview

This project is a **mini AI-powered analytics platform** for Shopify stores.  
It allows store owners to ask **natural language questions** about inventory, sales, and customers, and get **human-readable insights**.

The system consists of:

1. **Rails API (Backend Gateway)**  
   - Handles Shopify OAuth authentication  
   - Accepts user questions via API  
   - Forwards requests to Python AI service  
   - Returns formatted JSON responses

2. **Python AI Service (Agentic Intelligence Layer)**  
   - LLM-powered agent for intent classification  
   - ShopifyQL query generation  
   - Query validation & execution  
   - Converts raw Shopify data into business-friendly explanations  
   - Returns answers with confidence scores

---

## Architecture

