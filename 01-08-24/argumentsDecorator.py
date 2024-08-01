# Write a decorator named logging_decorator that displays the arguments passed to a function and its return value. Use this decorator on a function that multiplies two numbers and returns the result.

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments:{args, kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logging_decorator
def add(num1, num2):
    return num1+num2

print(add(5,51))