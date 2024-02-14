def eat_cookie(presents_left, nice_kids):  # we use these parameters not to use global values
    for coordinates in directions.values():
        r = santa_position[0] + coordinates[0]
        c = santa_position[0] + coordinates[1]

        if matrix[r][c].isalpha():
            if matrix[r][c] == "V":
                nice_kids += 1

            matrix[r][c] = "-"
            presents_left -= 1
        if not presents_left:
            break

    return presents_left, nice_kids  # and we just return the result


presents = int(input())
n = int(input())

matrix = []
santa_position = []

total_nice_kids = 0
nice_kids_visited = 0

for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == "S":
            santa_position = [r, c]
            matrix[r][c] = "-"
        elif matrix[r][c] == "V":
            total_nice_kids += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    if command == "Christmas morning":
        break

    # move santa clause
    santa_position = [
        santa_position[0] + directions[command][0],
        santa_position[1] + directions[command][1]
    ]

    # check on what he has stepped
    house = matrix[santa_position[0]][santa_position[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1

    elif house == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    matrix[santa_position[0]][santa_position[1]] = "-"

        # again check if there are no more presents

    if not presents or nice_kids_visited == total_nice_kids:
        break


matrix[santa_position[0]][santa_position[1]] = "S"

if not presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row, sep=' ') for row in matrix]

if total_nice_kids == nice_kids_visited:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
