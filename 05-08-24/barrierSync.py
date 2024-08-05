import threading


def worker(barrier, id):
    print(f"Thread {id} waiting at the barrier")
    barrier.wait()
    print(f"Thread {id} passed the barrier")


num_threads = 3
barrier = threading.Barrier(num_threads)

threads = []
for i in range(num_threads):
    t = threading.Thread(target=worker, args=(barrier, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have passed the barrier")
