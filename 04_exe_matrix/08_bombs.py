n = int(input())

matrix = [[int(n) for n in input().split()] for r in range(n)]
# cast to int with tuple comprehension
coordinates = ([int(x) for x in coordinate.split(',')] for coordinate in input().split())

directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
    (-1, 1),  # top -right
    (-1, -1),  # top left
    (1, -1),  # bottom left
    (1, 1),  # bottom right
    (0, 0)  # current position (this should be last)
)

for bomb_r_idx, bomb_c_idx in coordinates:
    if matrix[bomb_r_idx][bomb_c_idx] <= 0:  # dead cell
        continue

    for x, y in directions:
        # coordinates for explosion points
        row_exp, col_exp = bomb_r_idx + x, bomb_c_idx + y

        # check which is a valid position to explode, a.k.a the explosion is in the matrix
        if 0 <= row_exp < n and 0 <= col_exp < n:
            matrix[row_exp][col_exp] -= matrix[bomb_r_idx][bomb_c_idx] if matrix[row_exp][col_exp] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row, sep=' ') for row in matrix]


