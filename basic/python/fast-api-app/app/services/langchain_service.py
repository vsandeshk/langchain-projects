from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from app.config import API_KEY

def setup_langchain_chat(model_name: str = "gemini-2.5-flash") -> ChatGoogleGenerativeAI:
    """Initialize LangChain-compatible Gemini chat model."""
    try:
        chat = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.0,
            google_api_key=API_KEY
        )
        return chat
    except Exception as e:
        raise RuntimeError(f"Error initializing LangChain chat: {e}")

# Initialize once for reuse
LANGCHAIN_CHAT = setup_langchain_chat()

def translate_text_with_style(chat, text: str, style: str) -> str:
    """Translate text into a given style using LangChain."""
    template = """Translate the text that is delimited by triple backticks
    into a style that is {style}.
    text: ```{text}```
    """
    prompt_template = ChatPromptTemplate.from_template(template)
    messages = prompt_template.format_messages(style=style, text=text)
    response = chat(messages)
    return response.content

def parse_review_with_schema(chat, review_text: str) -> dict:
    """Extract structured info from a review using LangChain output parser."""
    schemas = [
        ResponseSchema(name="gift", description="Was the item purchased as a gift? True/False."),
        ResponseSchema(name="delivery_days", description="Number of days for delivery, or -1 if not found."),
        ResponseSchema(name="price_value", description="Sentences about value or price, as a list."),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = output_parser.get_format_instructions()

    review_template = """For the following text, extract the following information:

    gift: Was the item purchased as a gift for someone else? 
    Answer True if yes, False if not or unknown.

    delivery_days: How many days did it take for the product to arrive? 
    If not found, output -1.

    price_value: Extract any sentences about the value or price,
    and output them as a comma separated Python list.

    text: {text}

    {format_instructions}
    """
    prompt = ChatPromptTemplate.from_template(review_template)
    messages = prompt.format_messages(text=review_text, format_instructions=format_instructions)
    response = chat(messages)
    return output_parser.parse(response.content)
