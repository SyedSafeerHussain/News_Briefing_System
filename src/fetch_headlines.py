import os
import requests
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()
API_KEY=os.getenv("NEWS_API_KEY")

# 2. Define the function to fetch headlines
def get_top_headlines(country: str='us',page_size: int =10,query: str=None):
    """
    Fetches top headlines from NewsAPI.

    Args:
        country (str): 2-letter country code (default "us").
        page_size (int): Number of articles to fetch (default 10).
        query (str): Optional keyword filter.

    Returns:
        List of dicts: [{'title': ..., 'url': ...}, ...]
    """
    url="https://newsapi.org/v2/top-headlines"
    params={
        "apiKey":API_KEY,
        "country":country,
        "pageSize":page_size
    }
    if query:
        params["q"]=query
    responce=requests.get(url,params=params)
    responce.raise_for_status()
    data=responce.json()
    headlines=[]
    for article in data.get("articles",[]):
        headlines.append({
            "title":article.get("title"),
            "url":article.get("url")
        })
    return headlines
if __name__=="__main__":
    items=get_top_headlines()
    for idx,item in enumerate(items,start=1):
        print(f"{idx}.{item['title']}-{item['url']}")
        