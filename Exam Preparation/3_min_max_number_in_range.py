numbers_list = list(map(int, input().split()))
start_index = int(input())
end_index = int(input())

# Extract the range from start_index to end_index (inclusive)
range_numbers = numbers_list[start_index:end_index + 1]

# Find max and min in the range
max_num = max(range_numbers)
min_num = min(range_numbers)

# Print the sum of max and min
print(max_num + min_num)

