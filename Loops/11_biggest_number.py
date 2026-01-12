n = int(input())
biggest = int(input())

for i in range(n - 1):
    number = int(input())
    if number > biggest:
        biggest = number

print(biggest)
