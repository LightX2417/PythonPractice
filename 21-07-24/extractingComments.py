# Write a Python script to fetch a webpage and extract comments from the HTML.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup, Comment

url = input("Enter url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all comments
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for comment in comments:
    print(comment)
