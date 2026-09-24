rejected_entries = 0

def get_valid_input():
    global rejected_entries
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
            return int(stock)




def main():
    print("This is a Smart Inventory Auditor."
          "\nIt will continuously prompt for Stock Quantity."
          "\nTo exit please type \"Quit\"")

    inventory = 0

    while True:

        stock = get_valid_input()

        if stock == "quit":
            break


main()