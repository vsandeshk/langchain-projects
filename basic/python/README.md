# Gemini LangChain Demo

A modular demonstration of using **Google’s Gemini Large Language Model (LLM)** both **directly** (via the `google-generativeai` SDK) and **indirectly** through the **LangChain** framework.  

This example walks you through:
- Configuring the Gemini API using environment variables  
- Running direct text generation using `google-generativeai`  
- Creating prompt templates and structured output using LangChain  
- Parsing and formatting LLM responses cleanly and reproducibly  

---

## 🧰 Features

- ✅ Environment configuration using `.env`  
- ✅ Direct Gemini API text completions  
- ✅ LangChain-based prompt handling  
- ✅ Structured output extraction with `ResponseSchema`  
- ✅ Clear modular functions for easy reuse  

---

## 📂 Project Structure

```
.
├── gemini_langchain_demo.py    # Main demonstration script
├── .env                        # Contains GEMINI_API_KEY (not shared)
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignores venv, cache, and secrets
└── README.md                    # You are here
```

---

## ⚙️ Prerequisites

Before you start, ensure you have:

- Python **3.9+**  
- A valid **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey)  
- A virtual environment (recommended)  

---

## 🪄 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/gemini-langchain-demo.git
cd gemini-langchain-demo
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
# Create venv
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Your API Key
Create a file named `.env` in the project root:
```bash
touch .env
```

Add your Google Gemini API key inside it:
```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Demo

Once setup is complete, simply execute:
```bash
python gemini_langchain_demo.py
```

You should see:
- ✅ Confirmation of Gemini API setup  
- ✨ A direct Gemini completion (`What is 1 + 1?`)  
- 🌍 A translated customer email in an Italian polite tone  
- 🧩 Structured extraction (gift, delivery_days, price_value) from a review  

---

## 🧠 Code Highlights

### 🔹 Direct Gemini Usage
```python
response = get_completion("What is 1 + 1?")
```

### 🔹 LangChain Chat
```python
chat = setup_langchain_chat("gemini-2.5-flash", api_key)
```

### 🔹 Translation Example
```python
translate_text_with_style(chat, "Pirate-style complaint", "Italian polite tone")
```

### 🔹 Structured Output Parsing
```python
parse_review_with_schema(chat, "This blower arrived in 2 days, perfect for a gift!")
```

---

## 📦 Requirements

See [`requirements.txt`](./requirements.txt) for the list of core dependencies:
```
python-dotenv
google-generativeai
langchain
langchain-google-genai
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🧩 Troubleshooting

| Issue | Solution |
|-------|-----------|
| `❌ GEMINI_API_KEY not found` | Make sure `.env` exists and contains your API key. |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt`. |
| Output too long / cut off | Adjust model (e.g., `gemini-2.0-pro`) or prompt size. |

---

## 🧑‍💻 Author

**Your Name**  
📅 *Created on:* November 5, 2025  
💡 *Purpose:* Educational demo for using Gemini with LangChain  

---

## 📜 License

This project is open-source under the MIT License.  
Feel free to modify and use it for your own projects.

---

## 🌟 Example Output

```
✅ Gemini API configured successfully.
🔹 Direct Gemini API Test:
2

🔹 Translating Customer Email:
Il frullatore ha spruzzato ovunque! Ti prego di aiutarmi gentilmente.

🔹 Extracting structured data from review:
{'gift': True, 'delivery_days': 2, 'price_value': ['Slightly more expensive than others, but worth it.']}
```
