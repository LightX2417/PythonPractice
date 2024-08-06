# Create a simple program that uses the multiprocessing module to print the square of numbers from 0 to 9 using 5 different processes.

import multiprocessing

def print_square(num):
    print(f"Square of {num}: {num * num}")


if __name__ == "__main__":
    processes = []

    for i in range(10):
        process = multiprocessing.Process(target=print_square, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
