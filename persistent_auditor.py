rejected_entries = 0
num_delivery = 0


def load_inventory():
    try:
        file = open("inventory.txt", "r")

        inventory = int(file.readline().strip())

        file.close()

        return inventory

    except FileNotFoundError:
        return 0


def get_valid_input():
    global rejected_entries
    global num_delivery

    while True:
        stock = input("Enter Stock Quantity: ")

        if stock.lower() == "quit":
            return "quit"

        strip_stock = stock.strip("-")

        if stock.isdigit() == False and strip_stock.isdigit() == False:
            print("Stock quantity is invalid please only enter numbers.")
            rejected_entries += 1
            continue

        elif int(stock) < 0:
            print("Stock quantity is invalid please only enter positive numbers.")
            rejected_entries += 1
            continue

        else:
            num_delivery += 1
            return int(stock)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, total_delivery, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Deliveries Done: {total_delivery}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    print("This is a Smart Inventory Auditor."
          "\nIt will continuously prompt for Stock Quantity."
          "\nTo exit please type \"Quit\"")

    inventory = load_inventory()

    print(f"Loaded Inventory: {inventory}")

    while True:

        stock = get_valid_input()

        if stock == "quit":
            generate_report(inventory, num_delivery, rejected_entries)
            break

        inventory = process_delivery(inventory, stock)

        if inventory > 500:
            print("ALERT Overstock detected, total inventory has exceeded 500 units.")

        tax = calculate_tax(stock)
        print(f"Tax for this delivery: {tax}")


main()