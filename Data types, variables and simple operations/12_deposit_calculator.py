deposited_amount = float(input())
deposit_months = int(input())
annual_interest_rate = float(input())/100
final_amount = deposited_amount+deposit_months*((deposited_amount*annual_interest_rate)/12)
print(final_amount)