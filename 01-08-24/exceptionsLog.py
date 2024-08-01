# Write a function that divides two numbers and logs an exception if a division by zero occurs. The exception should be logged with the ERROR level.
import logging

# Set up basic logging configuration
logging.basicConfig(
    filename="exceptions.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero", exc_info=True)


# Test the function
result = divide(10, 2)
print(result)

result = divide(10, 0)
print(result)
