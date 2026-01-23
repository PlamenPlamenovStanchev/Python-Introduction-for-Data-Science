def check_the_room(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms+1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chairs += difference
    return free_chairs
count_of_room = int(input())
total_free_chairs = check_the_room(count_of_room)
if total_free_chairs >=0:
    print(f"Game On, {total_free_chairs} free chairs left")