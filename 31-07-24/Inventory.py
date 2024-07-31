# Create a program to manage a store's inventory using namedtuple to represent products and Counter to track inventory levels.

from collections import namedtuple, Counter

Product = namedtuple("Product", ["id", "name", "price"])
inventory = Counter()

# Adding products to inventory
products = [
    Product(1, "Apple", 0.5),
    Product(2, "Banana", 0.2),
    Product(3, "Orange", 0.3),
]

for product in products:
    inventory[product] += 10  # Adding 10 units of each product

# Selling some products
inventory[products[0]] -= 3  # Selling 3 apples
inventory[products[1]] -= 2  # Selling 2 bananas

# Display inventory levels
print("Inventory levels:")
for product, count in inventory.items():
    print(f"Product: {product.name}, Quantity: {count}, Price: ${product.price}")
