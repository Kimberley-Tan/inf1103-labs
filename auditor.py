print("This is a Smart Inventory Auditor. \nIt will continuously prompt for Stock Quantity.\nTo exit please type \"Quit\"")
inventory = 0
rejected_entries = 0
while True:
    stock = input("Enter Stock Quantity:")
    strip_stock = stock.strip("-")
    if stock == "Quit" or stock == "quit":
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Failed/Rejected Entries: {rejected_entries}")
        break
    if stock.isdigit() == False and strip_stock.isdigit() == False:
        print("Stock quantity is invalid please only enter numbers.")
        rejected_entries+=1
        continue
    elif int(stock)<0:
        print("Stock quantity is invalid please only enter positive numbers.")
        rejected_entries+=1
        continue
    else:
        inventory += int(stock)
        if inventory>500:
            print("ALERT Overstock detected, total inventory has exceeded 500 units.")
            break