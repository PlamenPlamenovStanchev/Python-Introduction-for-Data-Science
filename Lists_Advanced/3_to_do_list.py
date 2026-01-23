notes = [0] * 10  # Initialize a list with 10 empty notes

while True:
    command = input()
    if command == "End":
         break

    tokens = command.split("-")
    priority = int(tokens[0]) - 1  # Convert to zero-based index
    note = tokens[1]
    notes.pop(priority)  # Remove the existing note at the priority
    notes.insert(priority, note)  # Insert the new note at the priority

result = [note for note in notes if note != 0]  # Filter out empty notes
print(result)