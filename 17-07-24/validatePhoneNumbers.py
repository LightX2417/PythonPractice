# Write a Python function that validates phone numbers. Assume the phone number format is (xxx) xxx-xxxx.

import re

def validate_phone_number(phone_number):
    phone_pattern = r"\(\d{3}\) \d{3}-\d{4}"
    match = re.fullmatch(phone_pattern, phone_number)
    return bool(match)

phone_number = "(123) 456-7890"
print(validate_phone_number(phone_number))  
