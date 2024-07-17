# Write a Python function that finds all dates in a given text. Assume dates are in the format dd/mm/yyyy.

import re

def find_dates(text):
    date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    dates = re.findall(date_pattern, text)
    return dates

text = "Today's date is 17/07/2024 and tomorrow's date is 18/07/2024."
print(find_dates(text))  
