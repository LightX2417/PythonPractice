# Write a Python function that extracts all hashtags from a given text.

import re

def extract_hashtags(text):
    hashtag_pattern = r"#\w+"
    hashtags = re.findall(hashtag_pattern, text)
    return hashtags

text = "Loving the #weather today! #sunny #happy"
print(extract_hashtags(text)) 
