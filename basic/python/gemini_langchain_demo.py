# -*- coding: utf-8 -*-
"""
gemini_langchain_demo.py

A modular demonstration of using Google's Gemini LLM both directly
via the `google-generativeai` SDK and through the LangChain framework.

Features:
    - Environment variable setup with dotenv
    - Direct Gemini API prompt completion
    - LangChain prompt templating and structured output parsing

Author: Your Name
Date: 2025-11-05
"""

# ===============================================================
# Imports
# ===============================================================
import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser


# ===============================================================
# Configuration
# ===============================================================
def configure_api() -> str:
    """Load the environment variables and configure the Gemini API."""
    _ = load_dotenv(find_dotenv())
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")

    genai.configure(api_key=api_key)
    print("✅ Gemini API configured successfully.")
    return api_key


# ===============================================================
# Direct Gemini API Usage
# ===============================================================
def get_completion(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Generate a text completion directly using the Gemini API.

    Args:
        prompt (str): Input text prompt.
        model (str): Gemini model name (default: "gemini-2.5-flash").

    Returns:
        str: The generated response text.
    """
    model_instance = genai.GenerativeModel(model)
    response = model_instance.generate_content(prompt)
    return response.text


# ===============================================================
# LangChain Setup
# ===============================================================
def setup_langchain_chat(model_name: str, api_key: str) -> ChatGoogleGenerativeAI:
    """
    Initialize a LangChain-compatible Gemini chat model.

    Args:
        model_name (str): Gemini model name.
        api_key (str): Google Gemini API key.

    Returns:
        ChatGoogleGenerativeAI: Configured LangChain chat model instance.
    """
    chat = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.0,  # deterministic output
        google_api_key=api_key,
    )
    print(f"✅ LangChain chat model '{model_name}' initialized.")
    return chat


# ===============================================================
# Prompt Translation Example
# ===============================================================
def translate_text_with_style(chat, text: str, style: str) -> str:
    """
    Translate a given text into a specific style using LangChain prompts.

    Args:
        chat: LangChain Gemini chat model instance.
        text (str): Text to translate.
        style (str): Desired output style.

    Returns:
        str: Translated text.
    """
    template = """Translate the text that is delimited by triple backticks
    into a style that is {style}.
    text: ```{text}```
    """
    prompt_template = ChatPromptTemplate.from_template(template)
    messages = prompt_template.format_messages(style=style, text=text)
    response = chat(messages)
    return response.content


# ===============================================================
# Structured Output Parsing Example
# ===============================================================
def parse_review_with_schema(chat, review_text: str) -> dict:
    """
    Extract structured information (gift, delivery_days, price_value)
    from a product review using a LangChain output parser.

    Args:
        chat: LangChain Gemini chat model instance.
        review_text (str): Product review text.

    Returns:
        dict: Parsed structured data.
    """
    # Define response schema
    schemas = [
        ResponseSchema(name="gift", description="Was the item purchased as a gift? True/False."),
        ResponseSchema(name="delivery_days", description="Number of days for delivery, or -1 if not found."),
        ResponseSchema(name="price_value", description="Sentences about value or price, as a list."),
    ]

    output_parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = output_parser.get_format_instructions()

    # Template for structured extraction
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
    output_dict = output_parser.parse(response.content)
    return output_dict


# ===============================================================
# Demo Execution
# ===============================================================
def main():
    """Main entry point for the demo."""
    api_key = configure_api()
    model_name = "gemini-2.5-flash"

    # --- Direct Gemini API Test ---
    print("\n🔹 Direct Gemini API Test:")
    print(get_completion("What is 1 + 1?"))

    # --- LangChain Chat Setup ---
    chat = setup_langchain_chat(model_name, api_key)

    # --- Example 1: Translation ---
    customer_email = (
        "Arrr, I be fuming that me blender lid flew off and "
        "splattered me kitchen walls with smoothie! And to make "
        "matters worse, the warranty don't cover cleaning. Help!"
    )
    style = "Italian Language in a calm and respectful tone"

    print("\n🔹 Translating Customer Email:")
    translated_text = translate_text_with_style(chat, customer_email, style)
    print(translated_text)

    # --- Example 2: Structured Output Parsing ---
    customer_review = (
        "This leaf blower is amazing. It arrived in two days, just "
        "in time for my wife's anniversary present. Slightly more "
        "expensive than others, but worth it for the features."
    )
    print("\n🔹 Extracting structured data from review:")
    parsed_output = parse_review_with_schema(chat, customer_review)
    print(parsed_output)
    print(type(parsed_output))


# ===============================================================
# Script Entry Point
# ===============================================================
if __name__ == "__main__":
    main()
