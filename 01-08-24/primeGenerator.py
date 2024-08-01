# Implement a generator function prime_numbers(limit) that yields prime numbers up to a given limit.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num


# Example usage
for prime in prime_numbers(20):
    print(prime)
