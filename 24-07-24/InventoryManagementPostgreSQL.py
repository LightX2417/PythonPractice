# Create an inventory management system where you can:
# Add items with their name, category, and quantity.
# Update the quantity of an item.
# View all items and their details.

import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="example_db",
    user="example_user",
    password="example_password",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()

# Create table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name TEXT,
    category TEXT,
    quantity INTEGER
)
"""
)
conn.commit()


# Add a new item
def add_item(name, category, quantity):
    cursor.execute(
        """
    INSERT INTO items (name, category, quantity)
    VALUES (%s, %s, %s)
    """,
        (name, category, quantity),
    )
    conn.commit()


# Update item quantity
def update_item_quantity(item_id, new_quantity):
    cursor.execute(
        """
    UPDATE items
    SET quantity = %s
    WHERE id = %s
    """,
        (new_quantity, item_id),
    )
    conn.commit()


# View all items
def view_items():
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Example usage
add_item("Laptop", "Electronics", 10)
add_item("Desk Chair", "Furniture", 5)
update_item_quantity(1, 8)
view_items()

# Close the connection
cursor.close()
conn.close()
