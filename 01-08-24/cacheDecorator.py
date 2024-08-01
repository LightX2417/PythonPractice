# Create a cache_decorator that caches the results of a function so that if the function is called again with the same arguments, the cached result is returned instead of recalculating it. Apply this decorator to a function that computes the nth Fibonacci number.


def cache_decorator(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@cache_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(20))
