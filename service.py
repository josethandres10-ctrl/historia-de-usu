from validations import *
from functions import *
import csv

inventory = []


# Add products and store them in a list of dictionaries
def addProduct():
    
    valid_name = True
    while valid_name:
        print("")
        name = input("Enter product name: ").strip().lower()
        valid_name = validationProductName(name)

    valid_price = True
    while valid_price:
        try:
            print("")
            price = float(input("Enter product price: "))
            valid_price = validationNum(price)
        except ValueError:
            print("Error: enter a valid number")

    valid_qty = True
    while valid_qty:
        try:
            print("")
            quantity = int(input("Enter quantity: "))
            valid_qty = validationNum(quantity)
        except ValueError:
            print("Error: enter a valid number")

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)

    with open("inventory.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        file.seek(0, 2)
        if file.tell() == 0:
            writer.writerow(["name", "price", "quantity"])

        writer.writerow([name, price, quantity])


# Show products from CSV
def showInventory():
    with open("inventory.csv", mode="r") as file:
        print("")
        rows = file.readlines()

        for idx, row in enumerate(rows[1:], start=1):
            values = row.strip().split(",")

            if len(values) >= 3:
                name = values[0]
                price = float(values[1])
                quantity = int(values[2])

                print(f"{idx:<4} {name:<25} ${price:<10.2f} {quantity:<10}")


# Search product
def searchProduct():
    with open("inventory.csv", mode="r") as file:
        search_name = input("Enter product name: ").strip().lower()
        rows = file.readlines()
        found = False

        for idx, row in enumerate(rows[1:], start=1):
            values = row.strip().split(",")

            if values[0] == search_name:
                name = values[0]
                price = float(values[1])
                quantity = int(values[2])

                print("")
                print(f"{idx:<4} {name:<25} ${price:<10.2f} {quantity:<10}")
                found = True
                break

        if not found:
            print("Product not found.")


# Update product
def updateProduct():
    filename = "inventory.csv"

    try:
        with open(filename, "r") as file:
            rows = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return False

    search_name = input("Enter product name: ").strip().lower()
    updated_rows = []
    found = False

    for index, row in enumerate(rows):
        values = row.strip().split(",")

        if index == 0 or values[0] != search_name:
            updated_rows.append(row)
        else:
            found = True
            print(f"Updating: {values[0]}")

            new_name = input("New name: ").strip()
            new_price = float(input("New price: "))
            new_qty = int(input("New quantity: "))

            updated_rows.append(f"{new_name},{new_price},{new_qty}\n")
            print("Updated successfully")

    if not found:
        print("Product not found.")
        return False

    with open(filename, "w") as file:
        file.writelines(updated_rows)

    return True


# Delete product
def deleteProduct():
    filename = "inventory.csv"

    try:
        with open(filename, "r") as file:
            rows = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    name = input("Enter product to delete: ").strip().lower()
    new_rows = []
    removed = False

    for index, row in enumerate(rows):
        values = row.strip().split(",")

        if index == 0 or values[0] != name:
            new_rows.append(row)
        else:
            removed = True

    if removed:
        with open(filename, "w") as file:
            file.writelines(new_rows)
        print("Product deleted")
    else:
        print("Product not found")


# Calculate statistics
def calculateStatistics():
    total_value = 0
    total_products = 0

    with open("inventory.csv", mode="r") as file:
        rows = file.readlines()

        for row in rows[1:]:
            values = row.strip().split(",")

            price = float(values[1])
            quantity = int(values[2])

            total_value += calculateTotalProduct(price, quantity)
            total_products += quantity

    print(f"""
Total value: {total_value}
Total products: {total_products}
""")