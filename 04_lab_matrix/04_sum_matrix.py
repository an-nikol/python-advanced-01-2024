rows, cols = [int(num) for num in input().split(', ')]

matrix = []

for row_idx in range(rows):
    inner_list = [int(num) for num in input().split()]
    matrix.append(inner_list)


for col_idx in range(cols):
    el_in_row = []
    for row_idx in range(rows):
        el_in_row.append(matrix[row_idx][col_idx])
    print(sum(el_in_row))