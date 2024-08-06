# Create a program where multiple processes increment each element of a shared array by a specific value.

import multiprocessing


def increment_array(shared_array, increment_value, lock):
    for i in range(len(shared_array)):
        with lock:
            shared_array[i] += increment_value


if __name__ == "__main__":
    # Shared array with initial values
    shared_array = multiprocessing.Array("i", [0, 1, 2, 3, 4])
    lock = multiprocessing.Lock()
    processes = [
        multiprocessing.Process(target=increment_array, args=(shared_array, 5, lock)) for _ in range(3)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f"Shared array after increments: {list(shared_array)}")
