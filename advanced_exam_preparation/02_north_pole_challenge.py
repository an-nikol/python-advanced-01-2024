rows, cols = map(int, input().split(', '))
matrix = []
santa_r = 0
santa_c = 0
items_count = 0

items = {
    "D": 0,  # Decoration
    "G": 0,  # Gifts
    "C": 0,  # Cookies
}

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == 'Y':
            santa_r = row
            santa_c = col
        elif matrix[row][col] != '.':
            items_count += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while items_count > 0:

    command = input()
    if command == 'End':
        break

    direction, steps = command.split('-')

    for step_count in range(int(steps)):
        dir_r, dir_c = directions[direction]

        # Moving out - Place x
        matrix[santa_r][santa_c] = 'x'

        # resize - R
        santa_r = santa_r + dir_r
        if santa_r < 0:
            santa_r = rows - 1
        elif santa_r > rows - 1:
            santa_r = 0

        # resize - C
        santa_c = santa_c + dir_c
        if santa_c < 0:
            santa_c = cols - 1
        elif santa_c > cols - 1:
            santa_c = 0

        if matrix[santa_r][santa_c] not in ['.', 'x']:
            items[matrix[santa_r][santa_c]] += 1
            items_count -= 1
        matrix[santa_r][santa_c] = 'Y'

        if items_count <= 0:
            break
else:
    print("Merry Christmas!")

print(f"You've collected:"
      f"\n- {items['D']} Christmas decorations"
      f"\n- {items['G']} Gifts"
      f"\n- {items['C']} Cookies")

[print(' '.join(x)) for x in matrix]
