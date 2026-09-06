import requests

API_URL = "https://api.devpree.com.br/shorturl/"

def shorten_url(url):
    response = requests.put(
        url = f"{API_URL}/create",
        json = {
            "longUrl": url,
            "length": 6
        },
        timeout=5
    )

    return response.json().get("shortUrl")