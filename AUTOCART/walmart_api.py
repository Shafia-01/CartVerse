import requests
import os
from dotenv import load_dotenv
load_dotenv()  
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
BASE_URL = "https://serpapi.com/search.json"

def fetch_trending_products(query, num_results=5):
    if not SERPAPI_KEY:
        print("❌ API key not set")
        return []

    params = {
        "engine": "walmart",
        "query": query,
        "api_key": SERPAPI_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    results = []
    organic = data.get("organic_results", [])
    if not organic:
        print("❌ No organic results found.")
        return []

    for item in organic[:num_results]:
        results.append ({
            "title": item.get("title", "N/A"),
            "link": item.get("link") or f"https://www.walmart.com/search?q={query.replace(' ', '+')}",
            "price": item.get("price")})

    return results
