number_string = input().split(", ")
numbers_list = [int(num) for num in number_string]

positive_numbers_list = [str(num) for num in numbers_list if num >= 0]
negative_numbers_list = [str(num) for num in numbers_list if num < 0]
even_numbers_list = [str(num) for num in numbers_list if num % 2 == 0]
odd_numbers_list = [str(num) for num in numbers_list if num % 2 != 0]

print("Positive:", ", ".join(positive_numbers_list))
print("Negative:", ", ".join(negative_numbers_list))
print("Even:", ", ".join(even_numbers_list))
print("Odd:", ", ".join(odd_numbers_list))