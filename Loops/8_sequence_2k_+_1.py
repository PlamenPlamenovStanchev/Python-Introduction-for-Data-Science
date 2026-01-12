number = int(input())
result = 1

while True:
    print(result)
    result = result * 2 + 1
    if result > number:
        break