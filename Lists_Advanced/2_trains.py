# Read the number of wagons
num_wagons = int(input())

# Create a train with the given number of wagons, all containing 0 people
train = [0] * num_wagons

# Process commands until "End"
while True:
    command = input()

    if command == "End":
        break

    # Parse the command
    parts = command.split()
    action = parts[0]

    if action == "add":
        people = int(parts[1])
        train[-1] += people  # Add to the last wagon

    elif action == "insert":
        index = int(parts[1])
        people = int(parts[2])
        train[index] += people  # Add to the wagon at the given index

    elif action == "leave":
        index = int(parts[1])
        people = int(parts[2])
        train[index] -= people  # Remove from the wagon at the given index

# Print the final train
print(train)