from math import floor

n = int(input())

matrix = []

my_row = 0
my_col = 0

coins = 0
my_path = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            matrix[row][col] = "0"
            my_row = row
            my_col = col
            my_path.append([my_row, my_col])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    if coins >= 100:
        print(f"You won! You've collected {floor(coins)} coins.")
        break

    command = input()

    my_row = my_row + directions[command][0]
    my_col = my_col + directions[command][1]

    # if i go out of the left side of the field -> transported to the right side
    if my_row < 0:
        my_row = n - 1
    # if i go out of the right side of the field -> transported to the left side
    elif my_row > n - 1:
        my_row = 0

    if my_col < 0:
        my_col = n - 1
    elif my_col > n - 1:
        my_col = 0

    if matrix[my_row][my_col] == "X":
        my_path.append([my_row, my_col])
        coins /= 2
        print(f"Game over! You've collected {floor(coins)} coins.")
        break
    else:
        my_path.append([my_row, my_col])
        coins += int(matrix[my_row][my_col])
        matrix[my_row][my_col] = "0"

print("Your path:")
for coordinate in my_path:
    print(coordinate)
