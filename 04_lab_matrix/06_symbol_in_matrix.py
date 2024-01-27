n = int(input())

matrix = []

for i in range(n):
    inner_list = list(input())
    matrix.append(inner_list)

searched_symbol = input()
position = None

for row_idx in range(n):
    if position:
        break
    for col_idx in range(len(matrix[row_idx])):
        curr_el = matrix[row_idx][col_idx]
        if searched_symbol == curr_el:
            position = (row_idx, col_idx)
            print(position)
            break


if not position:
    print(f"{searched_symbol} does not occur in the matrix")
