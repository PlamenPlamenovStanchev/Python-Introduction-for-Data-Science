n = int(input())
divisible_by_2 = 0
divisible_by_3 = 0
divisible_by_4 = 0

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        divisible_by_2 += 1
    if number % 3 == 0:
        divisible_by_3 += 1
    if number % 4 == 0:
        divisible_by_4 += 1

percent_2 = (divisible_by_2 / n) * 100
percent_3 = (divisible_by_3 / n) * 100
percent_4 = (divisible_by_4 / n) * 100

print(f"{percent_2:.2f}%\n {percent_3:.2f}%\n {percent_4:.2f}%")

