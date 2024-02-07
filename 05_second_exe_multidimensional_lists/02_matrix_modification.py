n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(num) for num in input().split()])

while True:
    line = input().split()

    if line[0] == 'END':
        break

    command, row, col, value = line[0], int(line[1]), int(line[2]), int(line[3])
    # 0 <= n < len
    if 0 > row or row >= n or 0 > col or col >= n:
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

[print(*row, sep=' ') for row in matrix]
