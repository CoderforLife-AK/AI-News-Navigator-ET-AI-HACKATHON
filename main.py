from fastapi import FastAPI

# IMPORTS UPDATED FOR YOUR FOLDER NAMES
from Services.News import get_news
from Services.Ai import summarize_news, news_chat
from personalization import filter_news

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI News Navigator is running 🚀"}


@app.get("/news/{interest}")
def personalized_news(interest: str):

    news = get_news(interest)
    news = filter_news(news, interest)

    results = []

    for article in news:
        summary = summarize_news(article["description"])

        results.append({
            "title": article["title"],
            "summary": summary,
            "url": article["url"]
        })

    return {"personalized_news": results}

@app.get("/ask")
def ask_ai(question: str, topic: str = "technology"):

    news = get_news(topic)

    # combine all news text
    combined_news = " ".join(
        [article["description"] or "" for article in news]
    )

    answer = news_chat(question, combined_news)

    return {
        "question": question,
        "answer": answer
    }