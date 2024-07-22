# Write a Python script to fetch a webpage containing a list of items and extract the text of each item. Assume the items are contained within <li> tags.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all list items
tags = soup("li")
for tag in tags:
    print(tag.text)
