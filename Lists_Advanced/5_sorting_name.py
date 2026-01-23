names = input().split(", ")

# Sort the names:
# 1. Primary sort: by length in descending order (use negative length)
# 2. Secondary sort: alphabetically in ascending order
sorted_names = sorted(names, key=lambda name: (-len(name), name))

# Print the result
print(sorted_names)