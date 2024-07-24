import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
"""
)
conn.commit()

# Insert data into the table
cursor.execute(
    """
INSERT INTO users (name, age)
VALUES (?, ?)
""",
    ("Alice", 30),
)

cursor.execute(
    """
INSERT INTO users (name, age)
VALUES (?, ?)
""",
    ("Bob", 25),
)

conn.commit()

# Read data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Update data in the table
cursor.execute(
    """
UPDATE users
SET age = ?
WHERE name = ?
""",
    (32, "Alice"),
)

conn.commit()

# Delete data from the table
cursor.execute(
    """
DELETE FROM users
WHERE name = ?
""",
    ("Bob",),
)

conn.commit()

# Read data after update and delete
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the database connection
conn.close()
