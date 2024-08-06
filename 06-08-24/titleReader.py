# Create a program that uses multiprocessing to scrape data from multiple web pages concurrently. Each process should fetch the HTML content of a web page and print its title.

import multiprocessing
import requests
from bs4 import BeautifulSoup


def fetch_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    print(f"Title of {url}: {title}")


if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
    ]

    processes = [
        multiprocessing.Process(target=fetch_title, args=(url,)) for url in urls
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
