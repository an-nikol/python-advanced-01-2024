rows, cols = 5, 5

matrix = []
my_position = 0, 0
all_targets = 0

for r in range(rows):
    matrix.append(input().split())
    for c in range(cols):
        if matrix[r][c] == "A":
            my_position = [r, c]
        elif matrix[r][c] == "x":
            all_targets += 1


targets_down = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split()
    current_direction = command[1]

    if command[0] == "move":
        steps = int(command[2])

        new_row = 0
        new_col = 0

        if current_direction == "up":
            new_row = my_position[0] - steps
            new_col = my_position[1]

        elif current_direction == "down":
            new_row = my_position[0] + steps
            new_col = my_position[1]
        elif current_direction == "left":
            new_row = my_position[0]
            new_col = my_position[1] - steps
        elif current_direction == "right":
            new_row = my_position[0]
            new_col = my_position[1] + steps

        if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == ".":
            my_position = [new_row, new_col]

    elif command[0] == "shoot":
        new_shot_row = my_position[0] + directions[command[1]][0]
        new_shot_col = my_position[1] + directions[command[1]][1]

        while 0 <= new_shot_row < rows and 0 <= new_shot_col < cols:
            if matrix[new_shot_row][new_shot_col] == "x":
                matrix[new_shot_row][new_shot_col] = "."
                all_targets -= 1
                targets_down.append([new_shot_row, new_shot_col])
                break

            new_shot_row += directions[current_direction][0]
            new_shot_col += directions[current_direction][1]

        if all_targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

if all_targets > 0:
    print(f"Training not completed! {all_targets} targets left.")

[print(row) for row in targets_down]
