# Write a Python program to calculate the age of a person born on "1990-05-15".

from datetime import datetime

birth_date = datetime.strptime("1990-05-15", "%Y-%m-%d")
today = datetime.now()

age = (
    today.year
    - birth_date.year
    - ((today.month, today.day) < (birth_date.month, birth_date.day))
)
print("Age:", age)
