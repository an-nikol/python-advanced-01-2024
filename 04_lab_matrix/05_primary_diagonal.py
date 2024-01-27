n = int(input())

matrix = []

for row_idx in range(n):
    inner_list = [int(num) for num in input().split()]
    matrix.append(inner_list)

sum_diagonal = 0

for row in range(n):
    sum_diagonal += matrix[row][row]


print(sum_diagonal)