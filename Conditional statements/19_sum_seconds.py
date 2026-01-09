
# Read input - three athletes' times in seconds
time1 = int(input())
time2 = int(input())
time3 = int(input())

# Calculate total time in seconds
total_seconds = time1 + time2 + time3

# Convert to minutes and seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# Print result in format "minutes:seconds" with leading zero for seconds
print(f"{minutes}:{seconds:02d}")