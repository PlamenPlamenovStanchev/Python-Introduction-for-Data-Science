input_operator = input()
first_number = int(input())
second_number = int(input())

def calculate(operator, num1, num2):
    result = None
    if operator == "add":
        result=num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    elif operator == "multiply":
        result =  num1 * num2
    elif operator == "divide":
        result = int(num1 / num2)
    return result

print(calculate(input_operator, first_number, second_number))