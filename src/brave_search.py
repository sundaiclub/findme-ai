import requests
import os
import json
from dotenv import load_dotenv
from scraper import *

load_dotenv()

BRAVE_API_TOKEN = os.getenv('BRAVE_API_TOKEN')

def parse_brave_search_results(search_results):
    if search_results is None:
        return None
    results = search_results.get("web", {}).get("results", [])
    if len(results) == 0:
        return None
    return results


def brave_search(query, count=10):
    base_url = "https://api.search.brave.com/res/v1/web/search"

    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_TOKEN
    }

    params = {
        "q": query,
        "count": count,
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        # write the response to a file
        with open("brave_search_results.json", "w") as f:
            f.write(json.dumps(response.json()))
        return parse_brave_search_results(response.json()) if response.status_code == 200 else response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def brave_search_and_scrape(query, count=3):
    results = brave_search(query, count)
    results_data = {}
    for result in results:
        url = result.get('url')
        if url:
            results_data[url] = scrape_data(url)
    return results_data
