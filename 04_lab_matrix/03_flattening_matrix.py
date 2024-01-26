rows = int(input())

matrix = []


for i in range(rows):
    inner_list = [int(num) for num in input().split(', ')]
    matrix.append(inner_list)

flattened = []

for row_idx in range(len(matrix)):
    for col_idx in range(len(matrix[row_idx])):
        flattened.append(matrix[row_idx][col_idx])
print(flattened)
