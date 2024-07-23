import json
import requests

def loadJSONfromUrl(url):
    response = requests.get(url)
    data = response.json()
    return data

url = "https://api.github.com"
data = loadJSONfromUrl(url)
print(data)
