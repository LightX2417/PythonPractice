# Use the apply_async method of a Pool to run a function that calculates the cube of a number asynchronously. Collect the results and print them.

import multiprocessing


def calculate_cube(num):
    return num**3


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    results = [pool.apply_async(calculate_cube, args=(i,)) for i in range(10)]

    output = [result.get() for result in results]
    print(f"Cube results: {output}")
