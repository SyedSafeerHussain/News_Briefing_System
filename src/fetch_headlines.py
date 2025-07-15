import os
import requests
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()
API_KEY=os.getenv("NEWS_API_KEY")

# 2. Define the function to fetch headlines
def get_top_headlines(country: str = 'us', page_size: int = 10, query: str = None):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": API_KEY,
        "country": country,
        "pageSize": page_size
    }
    if query:
        params["q"] = query
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    headlines = []
    for article in data.get("articles", []):
        headlines.append({
            "title": article.get("title"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name", "Unknown"),
            "publishedAt": article.get("publishedAt", "Unknown")
        })
    return headlines

if __name__=="__main__":
    items=get_top_headlines()
    for idx,item in enumerate(items,start=1):
        print(f"{idx}.{item['title']}-{item['url']}")
        