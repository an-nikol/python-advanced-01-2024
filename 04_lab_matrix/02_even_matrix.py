rows = int(input())

matrix = []

for row_idx in range(rows):
    inner_list = [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    matrix.append(inner_list)

print(matrix)