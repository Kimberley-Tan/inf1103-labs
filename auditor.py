print("This is a Smart Inventory Auditor. \nIt will continuously prompt for Stock Quantity.\nTo exit please type \"Quit\"")
inventory = 0
while True:
    stock = input("Enter Stock Quantity:")
    if stock == "Quit" or stock == "quit":
        break