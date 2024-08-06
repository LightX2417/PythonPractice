import multiprocessing


def calculate_sum(numbers):
    return sum(numbers)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)

    ranges = [range(0, 10), range(10, 20), range(20, 30), range(30, 40)]
    results = [pool.apply(calculate_sum, args=(r,)) for r in ranges]

    for r, result in zip(ranges, results):
        print(f"Sum of {list(r)}: {result}")
