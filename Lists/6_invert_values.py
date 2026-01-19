string = input().split()
opposites = []
for element in string:
    opposite_number = -int(element)
    opposites.append(opposite_number)
print(opposites)