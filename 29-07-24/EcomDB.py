import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname='ecommerce_db',
    user='ecommerce_user',
    password='ecommerce_password',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    address TEXT,
    registration_date DATE DEFAULT CURRENT_DATE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) UNIQUE,
    contact_name VARCHAR(100),
    contact_email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    address TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    description TEXT,
    price NUMERIC(10, 2),
    category_id INTEGER REFERENCES categories(category_id),
    supplier_id INTEGER REFERENCES suppliers(supplier_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS product_inventory (
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER,
    price NUMERIC(10, 2)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    customer_id INTEGER REFERENCES customers(customer_id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS shipping_details (
    shipping_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    shipping_address TEXT,
    shipping_date TIMESTAMP,
    delivery_date TIMESTAMP,
    tracking_number VARCHAR(100)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS discounts (
    discount_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    discount_percentage NUMERIC(5, 2),
    start_date DATE,
    end_date DATE
)
''')
conn.commit()

# Insert sample data
cursor.execute('''
INSERT INTO categories (category_name)
VALUES
('Electronics'),
('Books'),
('Clothing')
ON CONFLICT (category_name) DO NOTHING
''')

cursor.execute('''
INSERT INTO suppliers (supplier_name, contact_name, contact_email, phone_number, address)
VALUES
('Tech Supplies Inc.', 'John Tech', 'john.tech@techsupplies.com', '555-1234', '123 Tech Street'),
('Book Haven', 'Jane Book', 'jane.book@bookhaven.com', '555-5678', '456 Book Avenue')
ON CONFLICT (contact_email) DO NOTHING
''')

cursor.execute('''
INSERT INTO products (product_name, description, price, category_id, supplier_id)
VALUES
('Smartphone', 'Latest model smartphone with advanced features.', 699.99, 1, 1),
('Laptop', 'High-performance laptop for gaming and work.', 1199.99, 1, 1),
('Novel', 'Bestselling novel by a famous author.', 19.99, 2, 2)
ON CONFLICT DO NOTHING
''')

cursor.execute('''
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '555-1122', '789 Elm Street'),
('Bob', 'Lee', 'bob.lee@example.com', '555-3344', '321 Oak Street')
ON CONFLICT (email) DO NOTHING
''')

cursor.execute('''
INSERT INTO orders (customer_id, status)
VALUES
(1, 'Pending'),
(2, 'Shipped')
ON CONFLICT DO NOTHING
''')

cursor.execute('''
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES
(1, 1, 1, 699.99),
(1, 3, 2, 19.99),
(2, 2, 1, 1199.99)
ON CONFLICT DO NOTHING
''')

cursor.execute('''
INSERT INTO reviews (product_id, customer_id, rating, comment)
VALUES
(1, 1, 5, 'Great smartphone, highly recommend!'),
(3, 2, 4, 'Interesting novel, but a bit slow at times.')
ON CONFLICT DO NOTHING
''')

cursor.execute('''
INSERT INTO product_inventory (product_id, quantity)
VALUES
(1, 50),
(2, 30),
(3, 100)
ON CONFLICT (product_id) DO NOTHING
''')

cursor.execute('''
INSERT INTO shipping_details (order_id, shipping_address, shipping_date, delivery_date, tracking_number)
VALUES
(2, '321 Oak Street', '2024-07-29', '2024-07-31', 'TRACK12345')
ON CONFLICT DO NOTHING
''')

cursor.execute('''
INSERT INTO discounts (product_id, discount_percentage, start_date, end_date)
VALUES
(1, 10.00, '2024-08-01', '2024-08-15'),
(2, 15.00, '2024-08-01', '2024-08-10')
ON CONFLICT DO NOTHING
''')

conn.commit()

# Fetch and display some data
cursor.execute('SELECT * FROM customers')
customers = cursor.fetchall()
for customer in customers:
    print(customer)

# Close the connection
cursor.close()
conn.close()
