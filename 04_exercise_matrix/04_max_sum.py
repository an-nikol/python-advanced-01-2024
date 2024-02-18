rows, cols = [int(num) for num in input().split()]

matrix = [[int(j) for j in input().split()] for i in range(rows)]

max_sum = float("-inf")
start_idx_max_row = 0
start_idx_max_col = 0

for row_idx in range(rows - 2):
    for col_idx in range(cols - 2):
        current_sum = 0
        for r_3x3 in range(row_idx, (row_idx + 2) + 1):
            for c_3x3 in range(col_idx, (col_idx + 2) + 1):
                current_sum += matrix[r_3x3][c_3x3]

        if current_sum > max_sum:
            max_sum = current_sum
            start_idx_max_row = row_idx
            start_idx_max_col = col_idx

print(f"Sum = {max_sum}")
max_submatrix = [matrix[r][start_idx_max_col:(start_idx_max_col + 2) + 1] for r in range(start_idx_max_row, (start_idx_max_row + 2) + 1)]

[print(*row)for row in max_submatrix]



