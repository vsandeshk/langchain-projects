from fastapi import FastAPI, HTTPException
from app.models import CompletionRequest, TranslateRequest, ReviewParseRequest
from app.services import gemini_api, langchain_service

app = FastAPI(
    title="Gemini LangChain API",
    description="API endpoints using Google Gemini LLM directly or via LangChain",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Gemini LangChain API is running. Use /docs for interactive API docs."}

@app.post("/gemini-completion")
async def api_gemini_completion(request: CompletionRequest):
    """Direct Gemini API text completion."""
    try:
        result = gemini_api.get_completion(request.prompt, request.model)
        return {"completion": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate-text")
async def api_translate_text(request: TranslateRequest):
    """Translate text into a specific style using LangChain."""
    try:
        result = langchain_service.translate_text_with_style(
            langchain_service.LANGCHAIN_CHAT, request.text, request.style
        )
        return {"translated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/parse-review")
async def api_parse_review(request: ReviewParseRequest):
    """Extract structured information from a product review using LangChain."""
    try:
        result = langchain_service.parse_review_with_schema(
            langchain_service.LANGCHAIN_CHAT, request.review_text
        )
        return {"parsed_review": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
