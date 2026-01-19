num = int(input())
numbers = []

for i in range(num):
    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []

for number in numbers:
    if command == "even":
        if number % 2 == 0:
            filtered_numbers.append(number)
    elif command == "odd":
        if number % 2 != 0:
            filtered_numbers.append(number)
    elif command == "positive":
        if number >= 0:
            filtered_numbers.append(number)
    elif command == "negative":
        if number < 0:
            filtered_numbers.append(number)
print(filtered_numbers)
