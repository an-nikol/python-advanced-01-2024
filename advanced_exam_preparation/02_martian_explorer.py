def invalid_idx(r, c):
    return 0 > r or r >= n or 0 > c or c >= n


def move_to_the_other_side(my_pos):
    moved_position = []

    # if he goes out of the right side
    if my_pos[1] >= n:
        moved_position = [my_pos[0], my_pos[1] - n]

    # if he goes out of the left side
    elif my_pos[1] < 0:
        moved_position = [my_pos[0], my_pos[1] + n]

    # if he goes out of the top side
    elif my_pos[0] < 0:
        moved_position = [my_pos[0] + n, my_pos[1]]

    # if he goes out of the bottom side
    elif my_pos[0] >= n:
        moved_position = [my_pos[0] - n, my_pos[1]]

    return moved_position


n = 6

matrix = []
my_position = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "E":
            my_position = [row, col]
            matrix[row][col] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
commands = input().split(", ")

has_found_water_deposit = False
has_found_metal_deposit = False
has_found_concrete_deposit = False

for command in commands:
    # move
    my_position = [
        my_position[0] + directions[command][0],
        my_position[1] + directions[command][1]
    ]

    # check for valid idx
    if invalid_idx(my_position[0], my_position[1]):
        my_position = move_to_the_other_side(my_position)

    if matrix[my_position[0]][my_position[1]] == "W":
        has_found_water_deposit = True
        print(f"Water deposit found at ({my_position[0]}, {my_position[1]})")

    elif matrix[my_position[0]][my_position[1]] == "M":
        has_found_metal_deposit = True
        print(f"Metal deposit found at ({my_position[0]}, {my_position[1]})")

    elif matrix[my_position[0]][my_position[1]] == "C":
        has_found_concrete_deposit = True
        print(f"Concrete deposit found at ({my_position[0]}, {my_position[1]})")

    elif matrix[my_position[0]][my_position[1]] == "R":
        print(f"Rover got broken at ({my_position[0]}, {my_position[1]})")
        break


if has_found_water_deposit and has_found_metal_deposit and has_found_concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")