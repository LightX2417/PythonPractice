# Write a generator function even_numbers(n) that yields the even numbers from 0 to n (inclusive).


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# Example usage
for even in even_numbers(10):
    print(even)
