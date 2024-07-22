# Write a Python script to fetch a webpage and extract metadata (contained in <meta> tags), printing the name and content attributes.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all meta tags
tags = soup("meta")
for tag in tags:
    print(tag.get("name", "No name"), ":", tag.get("content", "No content"))
