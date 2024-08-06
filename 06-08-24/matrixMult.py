import multiprocessing
import numpy as np


def matrix_multiply(A, B, result, start_row, end_row):
    for i in range(start_row, end_row):
        for j in range(B.shape[1]):
            result[i * B.shape[1] + j] = np.dot(A[i], B[:, j])


if __name__ == "__main__":
    A = np.random.rand(4, 4)
    B = np.random.rand(4, 4)

    # Shared array for result with size 16 (4x4 matrix)
    shared_result = multiprocessing.Array("d", 4 * 4)

    processes = []
    num_processes = 4
    chunk_size = A.shape[0] // num_processes

    for i in range(num_processes):
        start_row = i * chunk_size
        end_row = (i + 1) * chunk_size if i != num_processes - 1 else A.shape[0]
        process = multiprocessing.Process(
            target=matrix_multiply, args=(A, B, shared_result, start_row, end_row)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Convert the shared array back to a NumPy array for display
    result_array = np.frombuffer(shared_result.get_obj()).reshape(4, 4)
    print(f"Resultant Matrix:\n{result_array}")
