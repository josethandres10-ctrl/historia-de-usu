inventory = []

# Add product
def add_item():
    name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid data, try again\n")
        return

    if price <= 0 or quantity <= 0 or name == "":
        print("Invalid values\n")
        return

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    print("Product added!\n")


# Show inventory
def show_items():
    if len(inventory) == 0:
        print("Inventory is empty\n")
        return

    print("\n--- Inventory ---")
    for item in inventory:
        print(f"Product: {item['name']} | Price: {item['price']} | Quantity: {item['quantity']}")
    print()


# Calculate statistics
def get_statistics():
    if len(inventory) == 0:
        print("No products available\n")
        return

    total_value = 0
    total_quantity = 0

    for item in inventory:
        total_value += item["price"] * item["quantity"]
        total_quantity += item["quantity"]

    print("\n--- Statistics ---")
    print(f"Total value: {total_value}")
    print(f"Total products: {total_quantity}\n")


# Final comment (TASK 5)
# This program manages an inventory system using lists and dictionaries.
# It allows adding products, displaying them, and calculating statistics.
# The menu uses loops and conditionals to control the program flow.