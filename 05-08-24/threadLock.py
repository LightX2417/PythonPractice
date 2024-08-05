import threading

balance = 0
lock = threading.Lock()


def deposit(amount):
    global balance
    with lock:
        local_balance = balance
        local_balance += amount
        balance = local_balance


threads = []
for _ in range(5):
    t = threading.Thread(target=deposit, args=(100,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final balance: {balance}")
