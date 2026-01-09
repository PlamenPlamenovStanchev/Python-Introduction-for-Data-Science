num1 = float(input())
num2 = float(input())
num3 = float(input())

# Check if any number is zero
if num1 == 0 or num2 == 0 or num3 == 0:
    print("zero")
else:
    # Count negative numbers
    negative_count = 0
    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1

    # If odd number of negatives, product is negative
    if negative_count % 2 == 1:
        print("negative")
    else:
        print("positive")

