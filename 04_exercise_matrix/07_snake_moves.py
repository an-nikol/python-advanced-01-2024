from collections import deque

rows, cols = [int(num) for num in input().split()]
txt = deque(input())

matrix = []

for row_idx in range(rows):
    matrix.append([''] * cols)
    for col_idx in range(cols):
        if row_idx % 2 == 0:
            matrix[row_idx][col_idx] = txt[0]
        else:
            matrix[row_idx][-1-col_idx] = txt[0]
        txt. rotate(-1)
[print(*row, sep='') for row in matrix]



# rows, cols = [int(num) for num in input().split()]
# txt = list(input())
#
# matrix = []
#
# for row_idx in range(rows):
#     matrix.append([''] * cols)
#     for col_idx in range(cols):
#         if row_idx % 2 == 0:
#             matrix[row_idx][col_idx] = txt[0]
#             first_element = txt.pop(0)
#             txt.append(first_element)
#         else:
#             matrix[row_idx][-1 - col_idx] = txt[0]
#             first_element = txt.pop(0)
#             txt.append(first_element)
#
# [print(*row, sep='') for row in matrix]
