# Create an infinite generator function counter(start=0) that starts counting from start and yields consecutive numbers indefinitely.


def counter(start=0):
    count = start
    while True:
        yield count
        count += 1


# Example usage
gen = counter(10)
for _ in range(10):
    print(next(gen))
