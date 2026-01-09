balance = int(input())
withdrawal = int(input())
limit = int(input())

if withdrawal <= balance :
    print("The withdraw was successful." )
elif withdrawal > limit:
    print("The limit was exceeded.")
else:
    print("Insufficient availability.")