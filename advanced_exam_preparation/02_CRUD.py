rows = 6
cols = 6

matrix = [[col for col in input().split()]for r in range(rows)]

pos = input()

current_position = [int(x) for x in pos[1:-1].split(", ")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(", ")

    current_position = [
        current_position[0] + directions[command[1]][0],
        current_position[1] + directions[command[1]][1]
    ]

    if command[0] == "Create":

        if matrix[current_position[0]][current_position[1]] == ".":
            matrix[current_position[0]][current_position[1]] = command[2]

    elif command[0] == "Update":

        if matrix[current_position[0]][current_position[1]] != ".":
            matrix[current_position[0]][current_position[1]] = command[2]

    elif command[0] == "Delete":
        if matrix[current_position[0]][current_position[1]] != ".":
            matrix[current_position[0]][current_position[1]] = "."

    elif command[0] == "Read":
        if matrix[current_position[0]][current_position[1]] != ".":
            print(matrix[current_position[0]][current_position[1]])

[print(*row, sep=" ") for row in matrix]