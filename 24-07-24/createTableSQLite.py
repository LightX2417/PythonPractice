import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a new table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER
)
"""
)
conn.commit()

# Insert multiple records into the books table
books = [
    ("The Catcher in the Rye", "J.D. Salinger", 1951),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
]

cursor.executemany(
    """
INSERT INTO books (title, author, year)
VALUES (?, ?, ?)
""",
    books,
)
conn.commit()


