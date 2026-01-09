num1 = int(input())
num2 = int(input())
math_operator = input()  # "+", "-", "*", "/",

if math_operator == "+":
    result = num1 + num2
    print(f"{num1} {math_operator} {num2} = {result:.2f}")
elif math_operator == "-":
    result = num1 - num2
    print(f"{num1} {math_operator} {num2} = {result:.2f}")
elif math_operator == "*":
    result = num1 * num2
    print(f"{num1} {math_operator} {num2} = {result:.2f}")
elif math_operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
