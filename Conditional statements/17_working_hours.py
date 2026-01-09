
# Read input
hour = int(input())
day = input()

# Check if office is open
# Working hours: 10 AM to 6 PM (10 to 18), Monday to Saturday
if day == "Sunday":
    print("closed")
elif hour >= 10 and hour < 18:
    print("open")
else:
    print("closed")