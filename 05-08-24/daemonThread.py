import threading
import time


def background_task():
    while True:
        print("Running background task")
        time.sleep(1)


# Create daemon thread
t = threading.Thread(target=background_task)
t.daemon = True

# Start daemon thread
t.start()

# Main thread sleeps for 3 seconds
time.sleep(3)
print("Main thread exiting")
