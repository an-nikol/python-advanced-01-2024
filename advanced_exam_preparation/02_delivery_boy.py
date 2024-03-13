def is_invalid_index(r, c):
    return 0 > r or r >= rows or 0 > c or c >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []

my_position = []
starting_position = []
for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "B":
            my_position = [row, col]
            starting_position = [row, col]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    # move player
    next_position = [
        my_position[0] + directions[command][0],
        my_position[1] + directions[command][1]
    ]

    if is_invalid_index(next_position[0], next_position[1]):
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = " "
        break

    if matrix[next_position[0]][next_position[1]] == "P":
        matrix[next_position[0]][next_position[1]] = "R"
        my_position = next_position
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[next_position[0]][next_position[1]] == "*":
        continue

    elif matrix[next_position[0]][next_position[1]] == "A":
        matrix[next_position[0]][next_position[1]] = "P"
        my_position = next_position
        print("Pizza is delivered on time! Next order...")
        matrix[starting_position[0]][starting_position[1]] = "B"
        break
    else:
        matrix[next_position[0]][next_position[1]] = "."
        my_position = next_position


[print(''.join(row)) for row in matrix]