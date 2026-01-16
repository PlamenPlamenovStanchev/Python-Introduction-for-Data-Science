def validate_password(password):
    is_valid = True

    # Check length (6-10 characters)
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        is_valid = False

    # Check if consists only of letters and digits
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    # Check if has at least 2 digits
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    # If all validations passed
    if is_valid:
        print("Password is valid")


# Get input
password = input()

# Validate password
validate_password(password)