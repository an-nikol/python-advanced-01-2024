# check valid commands
def are_coordinates_valid(row1, col1, row2, col2, matr_rows, matr_cols):
    return 0 <= row1 < matr_rows and 0 <= col1 < matr_cols and 0 <= row2 < matr_rows and 0 <= col2 < matr_cols


# create matrix
rows, cols = [int(x) for x in input().split()]

matrix = [[c for c in input().split()] for r in range(rows)]

# operations with matrix

while True:
    line = input()
    if line == 'END':
        break

    commands = line.split()

    if commands[0] != 'swap' or len(commands) != 5:
        print('Invalid input!')
        continue

    r1, c1, r2, c2 = [int(n) for n in commands[1:]]

    if are_coordinates_valid(r1, c1, r2, c2, rows, cols):
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')
        continue
