# Create a decorator called timing_decorator that measures and prints the time a function takes to execute. Apply this decorator to a function that performs a simple task, like calculating the sum of all numbers from 1 to 1,000,000.

import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def sum_numbers():
    return sum(range(1, 1000001))


print(sum_numbers())
