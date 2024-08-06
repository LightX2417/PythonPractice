# Use a Manager to create a shared list that can be modified by multiple processes. Each process should append its process ID to the list.

import multiprocessing


def append_to_list(shared_list):
    shared_list.append(multiprocessing.current_process().pid)


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_list = manager.list()

    processes = [
        multiprocessing.Process(target=append_to_list, args=(shared_list,)) for _ in range(10)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f"Shared list: {shared_list}")
