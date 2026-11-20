import csv
import math
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if not math.isfinite(value) or value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.DictReader(file)
            for row_number, row in enumerate(reader, start=2):
                try:
                    product = ProductFactory.create(
                        row["product_type"], row["product_id"], row["name"],
                        float(row["price"]), int(row["stock_quantity"]), supplier
                    )
                    if not inventory.add_product(product):
                        raise ValueError("Duplicate product ID")
                    loaded += 1
                except (ValueError, KeyError, TypeError) as error:
                    print(f"Skipping row {row_number}: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
