rows, cols = [int(num) for num in input().split()]

matrix = []

for row_idx in range(rows):
    inner_list = input().split()
    matrix.append(inner_list)

counter_submatr = 0

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        starting_symbol = matrix[row_idx][col_idx]
        right_symbol = matrix[row_idx][col_idx + 1]
        below_symbol = matrix[row_idx + 1][col_idx]
        diagonal_symbol = matrix[row_idx + 1][col_idx + 1]

        if starting_symbol == right_symbol == below_symbol == diagonal_symbol:
            counter_submatr += 1

print(counter_submatr)


