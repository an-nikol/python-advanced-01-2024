n = int(input())

bunny = [0, 0]
matrix = []

for r in range(n):
    matrix.append([symbol for symbol in input().split()])
    for c in range(n):
        if matrix[r][c] == "B":
            bunny = [r, c]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_direction = ''
max_eggs_matrix = []
max_eggs = float('-inf') # if a negative number is given in the input the max will always be 0

for direction, move in directions.items():
    current_eggs = 0
    current_eggs_matrix = []

    row_moved = bunny[0] + move[0]
    col_moved = bunny[1] + move[1]

    while 0 <= row_moved < n and 0 <= col_moved < n:
        if matrix[row_moved][col_moved] == 'X':
            break
        current_eggs += int(matrix[row_moved][col_moved])
        current_eggs_matrix.append([row_moved, col_moved])
        # WHEN YOU MOVE CHANGE THE POSITION
        row_moved += move[0]
        col_moved += move[1]

    if current_eggs >= max_eggs:  # and current_eggs_matrix: # if this is empty it means you didn't move the bunny,
        max_eggs = current_eggs
        max_eggs_matrix = current_eggs_matrix
        max_direction = direction

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)