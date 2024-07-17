# Write a Python function that extracts all email addresses from a given text.

import re

def extract_emails(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    return emails

text = "Please contact us at support@example.com and sales@example.org."
print(extract_emails(text))  
