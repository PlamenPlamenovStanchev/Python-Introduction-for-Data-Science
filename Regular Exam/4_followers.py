followers = {}

while True:
    command = input()
    if command == "Log out":
        break

    parts = command.split(": ")
    cmd = parts[0]
    username = parts[1]

    if cmd == "New follower":
        if username not in followers:
            followers[username] = 0

    elif cmd == "Like":
        count = int(parts[2])
        if username not in followers:
            followers[username] = count
        else:
            followers[username] += count

    elif cmd == "Comment":
        if username not in followers:
            followers[username] = 1
        else:
            followers[username] += 1

    elif cmd == "Blocked":
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")
for user, count in followers.items():
    print(f"{user}: {count}")