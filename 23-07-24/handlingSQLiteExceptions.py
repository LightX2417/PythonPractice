import sqlite3

try:
    # Connect to SQLite database
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # Intentional error: inserting into a non-existing table
    cursor.execute("INSERT INTO non_existing_table (name, age) VALUES ('Eve', 40)")

    # Commit the changes
    conn.commit()
except sqlite3.Error as error:
    print("Error occurred:", error)
finally:
    # Ensure the connection is closed even if there was an error
    if conn:
        conn.close()
