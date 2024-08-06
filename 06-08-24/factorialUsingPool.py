# Use a Pool to create multiple processes that calculate the factorial of numbers from 1 to 5. Print the results.

import multiprocessing
import math


def calculate_factorial(num):
    return math.factorial(num)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool(processes=5)
    results = pool.map(calculate_factorial, numbers)

    for num, result in zip(numbers, results):
        print(f"Factorial of {num}: {result}")
