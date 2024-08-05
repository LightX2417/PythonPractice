import threading
import requests
from bs4 import BeautifulSoup


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    print(f"Title of {url}: {title}")


urls = [
    "https://play.pokemonshowdown.com/",
    "https://www.youtube.com/",
    "https://www.geeksforgeeks.org/",
]

threads = []
for url in urls:
    t = threading.Thread(target=scrape_page, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Web scraping completed!")
