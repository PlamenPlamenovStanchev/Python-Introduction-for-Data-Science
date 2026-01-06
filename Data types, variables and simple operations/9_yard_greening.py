# Yard Greening - Calculate landscaping costs with discount

# Input
square_meters = float(input())

# Prices and discount
price_per_sqm = 7.61  # lv per square meter
discount_rate = 0.18  # 18% discount

# Calculate total cost before discount
total_cost = square_meters * price_per_sqm

# Calculate discount amount
discount = total_cost * discount_rate

# Calculate final price after discount
final_price = total_cost - discount

# Output
print(f"The final price is: {final_price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")

