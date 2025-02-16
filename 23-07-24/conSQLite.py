import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"""
)

# Insert a row of data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")

# Commit the changes
conn.commit()

# Query the database
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
