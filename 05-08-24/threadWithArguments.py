import threading


def greet(name):
    print(f"Hello, {name}!")

t = threading.Thread(target=greet, args=("Alice",))

t.start()

t.join()

print("Greeting complete!")
