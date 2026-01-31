count_of_days = int(input())

if count_of_days <=0:
    print(0)
else:
    total_water_consumed = 0

    for day in range(1, count_of_days + 1):
        liters_per_day = float(input())
        total_water_consumed += liters_per_day
        print(int(total_water_consumed))
