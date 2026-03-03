import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Connection": "keep-alive"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)