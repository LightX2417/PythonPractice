from concurrent.futures import ThreadPoolExecutor


def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, numbers)

print(list(results))
