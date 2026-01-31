numbers_list = list(map(int, input().split( )))
num = int(input())

bigger_numbers = [number for number in numbers_list if number > num]
print(" ".join(map(str, bigger_numbers)))