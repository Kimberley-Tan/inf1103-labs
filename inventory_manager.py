import json
from pathlib import Path
from product import Product
from inventory import Inventory

FILE_PATH = Path(__file__).with_name("inventory.json")


def load_inventory():
    inventory = Inventory()
    if not FILE_PATH.exists():
        print("inventory.json not found. Starting with an empty inventory.")
        return inventory
    print("inventory.json found.")
    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            records = json.load(file)
        if not isinstance(records, list):
            raise ValueError("Invalid inventory format")
        for item in records:
            if not isinstance(item, dict) or not all(k in item for k in ("id", "name", "price", "stock")):
                raise ValueError("Invalid inventory format")
            if isinstance(item["stock"], bool) or not isinstance(item["stock"], int):
                raise ValueError("Stock must be an integer")
            if not inventory.add_product(Product(item["id"], item["name"], item["price"], item["stock"])):
                raise ValueError("Duplicate product ID")
        print("Inventory loaded successfully.")
    except (OSError, json.JSONDecodeError, ValueError, TypeError) as error:
        print(f"Could not load inventory: {error}")
        print("Starting with an empty inventory.")
        return Inventory()
    return inventory


def save_inventory(inventory):
    try:
        with FILE_PATH.open("w", encoding="utf-8") as file:
            json.dump(inventory.to_list(), file, indent=4)
        print("Inventory saved successfully to inventory.json.")
        return True
    except OSError as error:
        print(f"Error saving inventory: {error}")
        return False


def read_nonnegative_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            if value < 0 or (number_type is float and value != value):
                print("Value cannot be negative or NaN.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def add_product(inventory):
    print("\nAdd New Product")
    while True:
        product_id = input("Product ID: ").strip().upper()
        if not product_id:
            print("Product ID cannot be empty.")
        elif inventory.search_product(product_id):
            print("Product ID already exists.")
        else:
            break
    while True:
        name = input("Product Name: ").strip()
        if name:
            break
        print("Product name cannot be empty.")
    price = read_nonnegative_number("Price: ", float)
    stock = read_nonnegative_number("Stock Quantity: ", int)
    inventory.add_product(Product(product_id, name, price, stock))
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return
    print(f"\nProduct Found:\nName: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
    product.update_stock(read_nonnegative_number("New Stock Quantity: ", int))
    print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return
    print("\nProduct Found\n" + "-" * 48)
    product.display_information()
    print("-" * 48)


def main():
    print("=" * 40 + "\nINVENTORY MANAGEMENT SYSTEM\n" + "=" * 40)
    inventory = load_inventory()
    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit")
        print("----------------------------")
        choice = input("Enter option: ").strip()
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            if save_inventory(inventory):
                print("Thank you for using Inventory Management System.\nProgram terminated.")
                break
            print("Save failed. Please resolve the error before exiting.")
        else:
            print("Invalid option. Please choose 1 to 6.")


if __name__ == "__main__":
    main()
