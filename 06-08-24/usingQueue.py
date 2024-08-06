# Write a program that creates a process to calculate the square of numbers from 0 to 9 and puts the results in a Queue. Another process should read from the Queue and print the results.

import multiprocessing


def calculate_square(numbers, queue):
    for n in numbers:
        queue.put(n * n)


def print_square(queue):
    while not queue.empty():
        print(f"Square: {queue.get()}")


if __name__ == "__main__":
    numbers = range(10)
    queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=calculate_square, args=(numbers, queue))
    process2 = multiprocessing.Process(target=print_square, args=(queue,))

    process1.start()
    process1.join()

    process2.start()
    process2.join()
