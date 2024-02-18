n = int(input())
matrix = [[int(num) for num in input().split()]for i in range(n)]
primary_diagonal = [matrix[row_idx][row_idx]for row_idx in range(n)]
secondary_diagonal = [matrix[row_idx][-row_idx - 1]for row_idx in range(n)] #n - i- 1

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)