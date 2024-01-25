rows, cols = [int(num)for num in input().split(', ')]

matrix = []

total_sum = 0
for row_idx in range(rows):
    inner_list = [int(num) for num in input().split(', ')]
    matrix.append(inner_list)
    total_sum += sum(inner_list)

print(total_sum)
print(matrix)