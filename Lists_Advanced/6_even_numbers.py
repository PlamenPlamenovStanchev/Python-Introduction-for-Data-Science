numbers_list = list(map(int, input().split(", ")))

found_indexes = map(lambda x: x if numbers_list[x] % 2 == 0 else "no", range(len(numbers_list)))

even_indexes = list(filter(lambda x: x != "no", found_indexes))

print(even_indexes)