# Write a Python function that replaces all HTML tags in a given string with an empty string.

import re

def remove_html_tags(text):
    html_pattern = r"<[^>]+>"
    clean_text = re.sub(html_pattern, "", text)
    return clean_text

html_text = "<p>This is a <b>bold</b> paragraph.</p>"
print(remove_html_tags(html_text))  
