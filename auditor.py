print("This is a Smart Inventory Auditor. \nIt will continuously prompt for Stock Quantity.\nTo exit please type \"Quit\"")
inventory = 0
while True:
    stock = input("Enter Stock Quantity:")
    strip_stock = stock.strip("-")
    if stock == "Quit" or stock == "quit":
        break
    if stock.isdigit() == False and strip_stock.isdigit() == False:
        print("Stock quantity is invalid please only enter numbers.")
        continue
    elif int(stock)<0:
        print("Stock quantity is invalid please only enter positive numbers.")
        continue
    else:
        inventory += int(stock)
        if inventory>500:
            print("ALERT Overstock detected, inventory has exceeded 500 items.")
            break