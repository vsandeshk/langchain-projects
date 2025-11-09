# 🚀 FastAPI + LangChain + Gemini API

This project provides a FastAPI-based interface to interact with **Google’s Gemini LLM** via **LangChain**.  
It exposes multiple endpoints to generate completions, translate text, and parse structured data from reviews.

---

## ⚙️ Requirements

- Python 3.9 or higher  
- Google Gemini API key  

---

## 🧩 1. Setup Environment

```bash
# Go to your project folder
cd python/fast-api-app

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate         # macOS / Linux
# or
venv\Scripts\activate            # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🔑 2. Environment Variables

Create a `.env` file in the same folder as your `main.py`:

```bash
touch .env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

## 🚀 3. Run the Server

If your `main.py` file is in the current folder:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

If `main.py` is inside a subpackage (like `fast_api_app/main.py`), run:

```bash
python3 -m uvicorn fast_api_app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ Once running, open your browser:

```
http://127.0.0.1:8000/docs
```

This opens the **interactive Swagger UI** for testing the APIs.

---

## 🧪 4. Example API Endpoints

### **1️⃣ Generate Completion**
**POST** `/api/gemini/completion`

Request:
```json
{
  "prompt": "Explain quantum computing in simple terms."
}
```

Response:
```json
{
  "response": "Quantum computing uses qubits that can represent both 0 and 1..."
}
```

---

### **2️⃣ Translate Text**
**POST** `/api/langchain/translate`

Request:
```json
{
  "text": "Arrr, me blender lid flew off!",
  "style": "Italian, polite tone"
}
```

Response:
```json
{
  "translated_text": "Sono molto dispiaciuto, il coperchio del mio frullatore è volato via!"
}
```

---

### **3️⃣ Parse Product Review**
**POST** `/api/langchain/parse-review`

Request:
```json
{
  "review_text": "It arrived in two days and was a perfect gift. A bit pricey but worth it."
}
```

Response:
```json
{
  "gift": true,
  "delivery_days": 2,
  "price_value": ["A bit pricey but worth it."]
}
```

---

## 🧰 5. Development Tips

- Restart automatically using `--reload`
- Swagger Docs → `/docs`
- ReDoc → `/redoc`
- If `GEMINI_API_KEY` not found → check `.env`
- To update dependencies:
  ```bash
  pip freeze > requirements.txt
  ```

---

## 🧼 6. Troubleshooting

| Issue | Cause | Fix |
|-------|--------|------|
| `ModuleNotFoundError` | Wrong working directory | Run from folder containing `main.py` |
| `command not found: uvicorn` | Not installed in venv | Reinstall: `pip install "uvicorn[standard]"` |
| `GEMINI_API_KEY not found` | Missing .env file | Add your Gemini API key to `.env` |

---

## 💡 7. Next Steps

- Add summarization, Q&A, or classification endpoints  
- Integrate logging, validation, and rate limiting  
- Deploy on Render, Google Cloud Run, or AWS Lambda  

---

**Author:** Sandesh Kumar  
📅 November 2025  
Built with ❤️ using FastAPI + LangChain + Gemini
