from collections import deque

people = deque()
total_water = int(input())

name = input()

while name != 'Start':
    people.append(name)
    name = input()

while True:
    command = input().split()
    if command[0] == 'End':
        break
    # refill
    elif command[0] == 'refill':
        total_water += int(command[1])
    else:
        needed_water = int(command[0])
        if total_water >= needed_water:
            total_water -= needed_water
            last_person = people.popleft()
            print(f"{last_person} got water")
        else:
            last_person = people.popleft()
            print(f"{last_person} must wait")

print(f"{total_water} liters left")