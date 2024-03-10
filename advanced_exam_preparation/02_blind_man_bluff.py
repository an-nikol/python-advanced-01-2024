def invalid_idx(r, c):
    return 0 > r or r >= rows or 0 > c or c >= cols


rows, cols = [int(n) for n in input().split()]

matrix = []
my_position = []

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "B":
            my_position = [row, col]
            matrix[row][col] = "-"

touched_opponents = 0
made_moves = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


while touched_opponents != 3:
    command = input()
    if command == "Finish":
        break

    # move
    next_position = [
        my_position[0] + directions[command][0],
        my_position[1] + directions[command][1]
    ]
    # valid idx
    if invalid_idx(next_position[0], next_position[1]) or matrix[next_position[0]][next_position[1]] == "O":
        continue

    elif matrix[next_position[0]][next_position[1]] == "P":
        matrix[next_position[0]][next_position[1]] = "-"
        touched_opponents += 1
        made_moves += 1
        my_position = next_position
    elif matrix[next_position[0]][next_position[1]] == "-":
        made_moves += 1
        my_position = next_position


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {made_moves}")
