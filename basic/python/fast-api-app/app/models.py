from pydantic import BaseModel

class CompletionRequest(BaseModel):
    prompt: str
    model: str = "gemini-2.5-flash"

class TranslateRequest(BaseModel):
    text: str
    style: str

class ReviewParseRequest(BaseModel):
    review_text: str
