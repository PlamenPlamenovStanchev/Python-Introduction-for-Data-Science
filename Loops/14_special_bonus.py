stop_number = int(input())
previous = None

while True:
    current = int(input())
    if current == stop_number:
        result = previous * 1.2
        print(int(result))
        break
    previous = current