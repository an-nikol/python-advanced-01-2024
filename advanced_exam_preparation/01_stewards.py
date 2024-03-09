from collections import deque

rotations = 0
seat_matches = []
seats = input().split(", ")

first_sequence = deque(int(x) for x in input().split(", "))
second_sequence = deque(int(x) for x in input().split(", "))


while len(seat_matches) != 3 and rotations != 10:
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()
    rotations += 1
    expected_match = chr(first_num + second_num)

    if str(first_num)+expected_match in seats:
        seat_matches.append(str(first_num) + expected_match)
        seats.remove(str(first_num)+expected_match)
    elif str(second_num) + expected_match in seats:
        seat_matches.append(str(second_num) + expected_match)
        seats.remove(str(second_num) + expected_match)
    else:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")