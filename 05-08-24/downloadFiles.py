# Write a program that downloads multiple files concurrently using multithreading.

import threading
import requests


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename}")


urls = [
    ("https://example.com/file1.txt", "file1.txt"),
    ("https://example.com/file2.txt", "file2.txt"),
    ("https://example.com/file3.txt", "file3.txt"),
]

threads = []
for url, filename in urls:
    t = threading.Thread(target=download_file, args=(url, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads completed!")
