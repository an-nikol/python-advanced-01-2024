rows, cols = [int(num) for num in input().split(', ')]

matrix = []

for i in range(rows):
    inner_list = [int(num) for num in input().split(', ')]
    matrix.append(inner_list)

result = float('-inf')
max_sum_sub_matrix = []
for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        main_symbol = matrix[row_idx][col_idx]
        right_symbol = matrix[row_idx][col_idx + 1]
        down_symbol = matrix[row_idx + 1][col_idx]
        diagonal_symbol = matrix[row_idx + 1][col_idx + 1]
        curr_sum = main_symbol + right_symbol + down_symbol + diagonal_symbol

        if curr_sum > result:
            result = curr_sum
            max_sum_sub_matrix = [[main_symbol, right_symbol], [down_symbol, diagonal_symbol]]

print(*max_sum_sub_matrix[0])
print(*max_sum_sub_matrix[1])
print(result)