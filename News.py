import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news(topic: str):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data.get("articles", [])[:5]:
        articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url")
        })

    return articles