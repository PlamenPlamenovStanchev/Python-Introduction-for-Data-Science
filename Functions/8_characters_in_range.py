def get_chars_between(char1, char2):
    # Get ASCII values
    start = ord(char1)
    end = ord(char2)

    # Ensure start is less than end
    if start > end:
        start, end = end, start

    # Generate all characters between (exclusive of endpoints)
    chars = [chr(i) for i in range(start + 1, end)]

    # Return as space-separated string
    return ' '.join(chars)


# Get input
char1 = input()
char2 = input()

# Get and print result
result = get_chars_between(char1, char2)
print(result)