# Create a program where multiple processes increment a shared integer value by 1. Use a lock to synchronize access to the shared value.

import multiprocessing


def increment_value(shared_value, lock):
    for _ in range(1000):
        with lock:
            shared_value.value += 1


if __name__ == "__main__":
    shared_value = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()

    processes = [
        multiprocessing.Process(target=increment_value, args=(shared_value, lock)) for _ in range(10)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f"Final shared value: {shared_value.value}")
