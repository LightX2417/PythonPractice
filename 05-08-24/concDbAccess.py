# Write a program that performs concurrent read and write operations on a SQLite database using multithreading.

import threading
import sqlite3


def create_table():
    conn = sqlite3.connect("example.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)"""
    )
    conn.commit()
    conn.close()


def insert_data(value):
    conn = sqlite3.connect("example.db")
    c = conn.cursor()
    c.execute("INSERT INTO data (value) VALUES (?)", (value,))
    conn.commit()
    conn.close()
    print(f"Inserted: {value}")


def read_data():
    conn = sqlite3.connect("example.db")
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    rows = c.fetchall()
    conn.close()
    print(f"Read data: {rows}")


create_table()

threads = []
for i in range(5):
    t = threading.Thread(target=insert_data, args=(f"Value {i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

t = threading.Thread(target=read_data)
t.start()
t.join()

print("Database operations completed!")
