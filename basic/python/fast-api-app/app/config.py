import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

def configure_gemini_api() -> str:
    """Load environment variables and configure Gemini API."""
    _ = load_dotenv(find_dotenv())
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("❌ GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)
    return api_key

# Initialize API key at import
API_KEY = configure_gemini_api()
