# python
bakery = {}
total_sold = 0

while True:
    line = input()
    if line == "Complete":
        break

    parts = line.split(maxsplit=2)
    cmd = parts[0]
    qty = int(parts[1])
    food = parts[2]

    if cmd == "Receive":
        if qty > 0:
            bakery[food] = bakery.get(food, 0) + qty

    elif cmd == "Sell":
        if food not in bakery:
            print(f"You do not have any {food}.")
        else:
            if bakery[food] < qty:
                sold_quantity = bakery[food]
                total_sold += sold_quantity
                del bakery[food]
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
            else:
                bakery[food] -= qty
                total_sold += qty
                print(f"You sold {qty} {food}.")
                if bakery[food] == 0:
                    del bakery[food]

for item, quantity in bakery.items():
    print(f"{item}: {quantity}")
print(f"All sold: {total_sold} goods")