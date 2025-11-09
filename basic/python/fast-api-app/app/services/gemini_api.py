import google.generativeai as genai

def get_completion(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """Generate text completion using Gemini API."""
    try:
        model_instance = genai.GenerativeModel(model)
        response = model_instance.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Error generating completion: {e}")
