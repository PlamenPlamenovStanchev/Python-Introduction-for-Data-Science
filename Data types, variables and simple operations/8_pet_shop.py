# Pet Shop - Calculate total expenses for dog and cat food

# Input
dog_food_packages = int(input())
cat_food_packages = int(input())

# Prices
dog_food_price = 2.50  # lv per package
cat_food_price = 4     # lv per package

# Calculate total cost
total_cost = (dog_food_packages * dog_food_price) + (cat_food_packages * cat_food_price)

# Output
print(f"{total_cost} lv.")

