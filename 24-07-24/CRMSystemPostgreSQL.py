# Create a CRM system to manage customers and their interactions. You should be able to:
# Add customers with their contact information.
# Log interactions (e.g., calls, emails) with customers.
# View all interactions for a specific customer.

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

# Create tables
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS interactions (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    interaction_type TEXT,
    details TEXT,
    interaction_date DATE
)
"""
)
conn.commit()


# Add a customer
def add_customer(name, email, phone):
    cursor.execute(
        """
    INSERT INTO customers (name, email, phone)
    VALUES (%s, %s, %s)
    """,
        (name, email, phone),
    )
    conn.commit()


# Log an interaction
def log_interaction(customer_id, interaction_type, details, interaction_date):
    cursor.execute(
        """
    INSERT INTO interactions (customer_id, interaction_type, details, interaction_date)
    VALUES (%s, %s, %s, %s)
    """,
        (customer_id, interaction_type, details, interaction_date),
    )
    conn.commit()


# View all interactions for a customer
def view_interactions(customer_id):
    cursor.execute(
        """
    SELECT * FROM interactions
    WHERE customer_id = %s
    """,
        (customer_id,),
    )
    interactions = cursor.fetchall()
    for interaction in interactions:
        print(interaction)


# Example usage
add_customer("Alice Johnson", "alice@example.com", "555-1234")
add_customer("Bob Lee", "bob@example.com", "555-5678")
log_interaction(1, "Call", "Discussed new features", "2024-07-24")
view_interactions(1)

# Close the connection
cursor.close()
conn.close()
