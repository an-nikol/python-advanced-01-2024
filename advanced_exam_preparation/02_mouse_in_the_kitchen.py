def is_invalid_index(r, c):
    return 0 > r or r >= rows or 0 > c or c >= cols


rows, cols = [int(x) for x in input().split(",")]

matrix = []
mouse_position = []

total_cheese = 0
line = ''

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "M":
            mouse_position = [row, col]
            matrix[row][col] = "*"
        elif matrix[row][col] == "C":
            total_cheese += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


while total_cheese != 0:
    line = input()
    if line == "danger":
        break   # move
    next_position = [
        mouse_position[0] + directions[line][0],
        mouse_position[1] + directions[line][1]
    ]

    if is_invalid_index(next_position[0], next_position[1]):
        print("No more cheese for tonight!")
        break

    if matrix[next_position[0]][next_position[1]] == "C":
        matrix[next_position[0]][next_position[1]] = "*"
        mouse_position = next_position
        total_cheese -= 1
    elif matrix[next_position[0]][next_position[1]] == "T":
        matrix[next_position[0]][next_position[1]] = "*"
        mouse_position = next_position
        print("Mouse is trapped!")
        break
    elif matrix[next_position[0]][next_position[1]] == "@":
        continue
    else: # if the moise steps on an empty position
        mouse_position = next_position
        continue

else:
    print("Happy mouse! All the cheese is eaten, good night!")


matrix[mouse_position[0]][mouse_position[1]] = "M"

if total_cheese and line == 'danger':
    print("Mouse will come back later!")

[print(*row, sep='') for row in matrix]