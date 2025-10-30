import requests

ONDC_BASE_URL = "https://sandbox.ondc.org"  # example; replace with actual

def get_products(category: str):
    url = f"{ONDC_BASE_URL}/catalog/search"
    payload = {
        "category": category
    }
    response = requests.post(url, json=payload)
    return response.json()

def search_products(query: str):
    url = f"{ONDC_BASE_URL}/catalog/search"
    payload = {
        "query": query
    }
    response = requests.post(url, json=payload)
    return response.json()
