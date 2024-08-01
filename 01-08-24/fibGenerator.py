# Create a generator function fibonacci(n) that yields the first n numbers in the Fibonacci sequence.


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Example usage
for num in fibonacci(10):
    print(num)
