DOLLARS_TO_LEVA = 1.57

cpu_price_in_dollars = float(input())
video_card_price_in_dollars = float(input())
ram_price_in_dollars = float(input())
ram_count = int(input())
discount = float(input())

discounted_cpu_price = cpu_price_in_dollars * (1 - discount)
discounted_video_card_price = video_card_price_in_dollars *(1-discount)

ram_price = ram_price_in_dollars * ram_count
total_sum_in_dollars = discounted_cpu_price + discounted_video_card_price + ram_price

total_sum_in_leva = total_sum_in_dollars * DOLLARS_TO_LEVA

print(f"Money needed - {total_sum_in_leva} leva.")