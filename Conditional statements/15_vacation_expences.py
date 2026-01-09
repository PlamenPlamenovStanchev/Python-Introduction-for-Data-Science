# Read input
season = input()
accommodation = input()
days = int(input())
price_per_night = 0
discount = 0.0

# Determine price per night and discount based on season and accommodation
if season == "Spring":
    discount = 0.20
    if accommodation == "Hotel":
        price_per_night = 30
    else:  # Camping
        price_per_night = 10
elif season == "Summer":
    discount = 0.00
    if accommodation == "Hotel":
        price_per_night = 50
    else:  # Camping
        price_per_night = 30
elif season == "Autumn":
    discount = 0.30
    if accommodation == "Hotel":
        price_per_night = 20
    else:  # Camping
        price_per_night = 15
elif season == "Winter":  # Winter
    discount = 0.10
    if accommodation == "Hotel":
        price_per_night = 40
    else:  # Camping
        price_per_night = 10

# Calculate total expenses
total_before_discount = days * price_per_night
total_expenses = total_before_discount * (1 - discount)

# Print result formatted to 2 decimal places
print(f"{total_expenses:.2f}")