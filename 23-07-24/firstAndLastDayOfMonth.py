from datetime import datetime, timedelta

# Get current date
current_date = datetime.now()

# Get first day of the month
first_day = current_date.replace(day=1)
first_day_str = first_day.strftime("%Y-%m-%d (%A)")

# Get last day of the month
next_month = current_date.replace(day=28) + timedelta(
    days=4
)  # this will always be in the next month
last_day = next_month - timedelta(days=next_month.day)
last_day_str = last_day.strftime("%Y-%m-%d (%A)")

print("First day of the month:", first_day_str)
print("Last day of the month:", last_day_str)
