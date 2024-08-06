# Create a program that searches for a specific keyword in multiple text files concurrently using multiprocessing. Print the file names that contain the keyword.

import multiprocessing

def search_keyword(file_path, keyword, result_list):
    with open(file_path, "r") as file:
        content = file.read()
        if keyword in content:
            result_list.append(file_path)


if __name__ == "__main__":
    text_files = ["file1.txt", "file2.txt", "file3.txt"]
    keyword = input("Enter search term: ")
    manager = multiprocessing.Manager()
    result_list = manager.list()

    processes = [
        multiprocessing.Process(
            target=search_keyword, args=(file, keyword, result_list)
        )
        for file in text_files
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f'Files containing the keyword "{keyword}": {list(result_list)}')
