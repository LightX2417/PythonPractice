import psycopg2
from psycopg2 import sql

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="example_db",
    user="example_user",
    password="example_password",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()

# Create a table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INTEGER
)
"""
)
conn.commit()


# Insert data
def insert_user(name, age):
    cursor.execute(
        """
    INSERT INTO users (name, age)
    VALUES (%s, %s)
    """,
        (name, age),
    )
    conn.commit()


# Read data
def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# Update data
def update_user_age(user_id, new_age):
    cursor.execute(
        """
    UPDATE users
    SET age = %s
    WHERE id = %s
    """,
        (new_age, user_id),
    )
    conn.commit()


# Delete data
def delete_user(user_id):
    cursor.execute(
        """
    DELETE FROM users
    WHERE id = %s
    """,
        (user_id,),
    )
    conn.commit()


# Example usage
insert_user("Alice", 30)
insert_user("Bob", 25)

print("All users:")
for user in get_all_users():
    print(user)

update_user_age(1, 31)
delete_user(2)

print("Users after update and delete:")
for user in get_all_users():
    print(user)

# Close the connection
cursor.close()
conn.close()
