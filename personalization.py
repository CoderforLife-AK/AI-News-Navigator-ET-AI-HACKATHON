def filter_news(articles, interest):

    personalized = []

    for article in articles:
        title = article["title"] or ""

        if interest.lower() in title.lower():
            personalized.append(article)

    return personalized if personalized else articles