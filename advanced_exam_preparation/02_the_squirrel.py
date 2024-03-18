def is_invalid_idx(r, c):
    return 0 > r or r >= n or 0 > c or c >= n


n = int(input())


commands = input().split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0 ,1)
}


matrix = []

my_position = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "s":
            my_position = [row, col]
            matrix[row][col] = "*"

collected_hazelnuts = 0


for command in commands:
    my_position = [
        my_position[0] + directions[command][0],
        my_position[1] + directions[command][1]
    ]
    if is_invalid_idx(my_position[0], my_position[1]):
        print("The squirrel is out of the field.")
        break

    elif matrix[my_position[0]][my_position[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    elif matrix[my_position[0]][my_position[1]] == "h":
        matrix[my_position[0]][my_position[1]] = "*"
        collected_hazelnuts += 1
        if collected_hazelnuts == 3:
            break
else:
    print("There are more hazelnuts to collect.")


if collected_hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {collected_hazelnuts}")