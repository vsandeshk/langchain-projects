# 🤖 LangChain + NestJS + Gemini Integration

This project demonstrates how to use **Google Gemini models** through **LangChain** in a modular **NestJS** application.

It is an exact Node.js (TypeScript) equivalent of the original Python-based `gemini_langchain_demo.py`.

---

## 📁 Project Structure

```
langchain-project/
├── src/
│   ├── langchain/
│   │   ├── langchain.service.ts      # Core LangChain logic
│   │   ├── langchain.controller.ts   # REST endpoints for Gemini
│   │   └── langchain.module.ts       # Module definition
│   └── main.ts                       # App entry point
├── .env                              # Environment variables
├── package.json                      # Dependencies and scripts
└── README.md                         # This file
```

---

## 🚀 Features

- Uses **LangChain + Google Gemini (Gemini 2.5 Flash)**.
- Modular **NestJS architecture** (Controller + Service + Module).
- Two key AI-powered endpoints:
  1. Text translation into a specified style.
  2. Structured product review parsing.

---

## ⚙️ Setup Instructions

### 1️⃣ install dependencies
```bash
npm install
```

### 2️⃣ Environment setup
Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 3️⃣ Run the app
```bash
npm run start:dev
```

Server starts at: **http://localhost:3000**

---

## 🔹 API Endpoints

### **POST /langchain/translate**
Translates text into a specific style using LangChain.

**Body:**
```json
{
  "text": "Arrr, I be fuming that me blender lid flew off!",
  "style": "Italian language in a calm and respectful tone"
}
```

**Response:**
```json
{
  "translated": "Sono molto arrabbiato che il coperchio del frullatore sia volato via..."
}
```

---

### **POST /langchain/parse-review**
Parses a product review into structured fields.

**Body:**
```json
{
  "review": "This leaf blower is amazing. It arrived in two days. A bit pricey but worth it."
}
```

**Response:**
```json
{
  "gift": true,
  "delivery_days": 2,
  "price_value": ["A bit pricey but worth it"]
}
```

---

## 🧩 Tech Stack

| Component | Library / Tool |
|------------|----------------|
| Backend Framework | NestJS 11 |
| LLM Integration | LangChain + @langchain/google-genai |
| Language | TypeScript (Node 18+) |
| Environment | dotenv |
| Validation | class-validator |

---

## 🧠 Notes

- Ensure Node.js 18+ is installed.
- LangChain and Google GenAI versions are kept at `^1.0.0` for compatibility.
- Modular structure allows easy extension (e.g., sentiment analysis, summarization).

---

## 🏁 Example Run

Once running, test endpoints via **Postman** or **cURL**:

### Translate Endpoint
```bash
curl -X POST http://localhost:3000/langchain/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello there!", "style": "Pirate tone"}'
```

### Parse Review Endpoint
```bash
curl -X POST http://localhost:3000/langchain/parse-review \
  -H "Content-Type: application/json" \
  -d '{"review": "It arrived in 3 days, was a gift, slightly expensive."}'
```

---

## 👤 Author

Created by **Sandesh Kumar**  
© 2025 — Built with ❤️ using **NestJS** and **LangChain**.

