# Write a decorator named retry_decorator that retries a function up to a specified number of times if it raises an exception. Apply this decorator to a function that simulates a task which may fail randomly, such as a function that raises an exception 50% of the time.

import random


def retry_decorator(retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
            print(f"All {retries} attempts failed.")

        return wrapper

    return decorator


@retry_decorator(3)
def unreliable_function():
    if random.random() < 0.5:
        raise ValueError("Random failure!")
    return "Success!"


print(unreliable_function())
