def is_valid_direction(starting_row, starting_col, row_dir, col_dir, size):
    return 0 <= starting_row + row_dir < size and 0 <= starting_col + col_dir < size


n = int(input())

current_directions = input().split()

matrix = [[ c for c in input().split()]for r in range(n)]

all_coal = 0

start_row, start_col = 0, 0

final_row, final_col = 0, 0

game_over = False


general_directions = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0]
}


for r in range(n):
    for c in range(n):
        if matrix[r][c] == 's':
            start_row = r
            start_col = c

        if matrix[r][c] == 'c':
            all_coal += 1


for direction in current_directions:
    if direction in general_directions:
        row_direction, col_direction = general_directions[direction]
        if is_valid_direction(start_row, start_col, row_direction, col_direction, n):
            start_row = start_row + row_direction
            start_col = start_col + col_direction
            final_row = start_row
            final_col = start_col

            if matrix[final_row][final_col] == 'c':
                all_coal -= 1
                matrix[final_row][final_col] = '*'
            if matrix[final_row][final_col] == 'e':
                print(f"Game over! ({final_row}, {final_col})")
                game_over = True
                break


if not game_over:
    if not all_coal:
        print(f"You collected all coal! ({final_row}, {final_col})")
    else:
        print(f"{all_coal} pieces of coal left. ({final_row}, {final_col})")


