string = input()
count = int(input())

repeat_string = lambda s, c: s * c
print(repeat_string(string, count))