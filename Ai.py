import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def summarize_news(text):

    if not text:
        return "No description available."

    prompt = f"""
    Summarize this business news simply.
    Explain why it matters in 4-5 lines.

    News:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text

def news_chat(question, combined_news):

    prompt = f"""
    You are an AI News Navigator.

    Based on the news below, answer the user's question clearly.

    NEWS DATA:
    {combined_news}

    USER QUESTION:
    {question}

    Give a clear, easy explanation.
    """

    response = model.generate_content(prompt)

    return response.text