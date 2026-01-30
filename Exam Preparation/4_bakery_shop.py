bakery = {}
total_sold = 0

while True:
    command = input()
    if command == "Complete":
        break

    parts = command.split()
    cmd = parts[0]
    qty = int(parts[1])
    food = parts[2]

    if cmd == "Receive":
        # Only add if quantity is valid (> 0)
        if qty > 0:
            if food not in bakery:
                bakery[food] = 0
            bakery[food] += qty

    elif cmd == "Sell":
        if food not in bakery:
            print(f"You do not have any {food}.")
        else:
            if bakery[food] < qty:
                # Sell what we have and remove the food
                sold_quantity = bakery[food]
                total_sold += sold_quantity
                del bakery[food]
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
            else:
                # Sell the requested quantity
                bakery[food] -= qty
                total_sold += qty
                print(f"You sold {qty} {food}.")
                # Remove food if stock becomes 0
                if bakery[food] == 0:
                    del bakery[food]

# Print final stock and total sold
output = ""
for item, quantity in bakery.items():
    output += f"{item}: {quantity} "
output += f"All sold: {total_sold} goods"
print(output)
