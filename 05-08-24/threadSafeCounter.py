import threading


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1


counter = Counter()


def worker():
    for _ in range(1000):
        counter.increment()


threads = []
for _ in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Counter value: {counter.value}")
