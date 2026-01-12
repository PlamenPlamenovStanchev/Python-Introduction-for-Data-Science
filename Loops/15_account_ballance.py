balance = 0.0

while True:
    input_data = input()
    if input_data == "End":
        break

    money = float(input_data)
    balance += money

    if money >= 0:
        print(f"Increase: {money:.2f}")
    else:
        print(f"Decrease: {abs(money):.2f}")

print(f"Balance: {balance:.2f}")