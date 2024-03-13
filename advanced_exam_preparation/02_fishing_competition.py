def is_index_invalid(r, c):
    return 0 > r or r >= n or 0 > c or c >= n


def move_to_the_other_side(my_pos):
    # if he escapes on the right side
    if my_pos[1] >= n:
        my_pos = [my_pos[0], my_pos[1] - n]
    # if he escapes the left side
    elif my_pos[1] < 0:
        my_pos = [my_pos[0], my_pos[1] + n]
    elif my_pos[0] >= n:
        my_pos = [my_pos[0] - n, my_pos[1]]
    elif my_pos[0] < 0:
        my_pos = [my_pos[0] + n, my_pos[1]]

    return my_pos


n = int(input())

matrix = []
sailor_pos = []
collected_fish = 0
goal_fish = 20

has_reached_the_quota = False
has_the_ship_sank = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "S":
            sailor_pos = [row, col]
            matrix[row][col] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    if command == "collect the nets":
        break

    # move sailor
    sailor_pos = [
        sailor_pos[0] + directions[command][0],
        sailor_pos[1] + directions[command][1]
    ]
    # check idx
    if is_index_invalid(sailor_pos[0], sailor_pos[1]):
        sailor_pos = move_to_the_other_side(sailor_pos)

    if matrix[sailor_pos[0]][sailor_pos[1]] == "W":
        has_the_ship_sank = True
        collected_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{','.join([str(x) for x in sailor_pos])}]")
        break
    elif matrix[sailor_pos[0]][sailor_pos[1]] != "-": # if it is a number
        collected_fish += int(matrix[sailor_pos[0]][sailor_pos[1]])
        matrix[sailor_pos[0]][sailor_pos[1]] = "-"
        if collected_fish >= goal_fish:
            has_reached_the_quota = True

if not has_the_ship_sank:
    matrix[sailor_pos[0]][sailor_pos[1]] = "S"
    if has_reached_the_quota:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {goal_fish - collected_fish} tons of fish more.")

    if collected_fish > 0:
        print(f"Amount of fish caught: {collected_fish} tons.")

    [print(*row, sep='') for row in matrix]







