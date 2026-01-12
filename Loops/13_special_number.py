num = int(input())
temp = num
is_special = True

while temp > 0:
    digit = temp % 10
    if num % digit != 0:
        is_special = False
        break
    temp = temp // 10

if is_special:
    print(f"{num} is special")
else:
    print(f"{num} is not special")