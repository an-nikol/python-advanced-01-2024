rows, cols = [int(x) for x in input().split()]

start_idx = ord('a')

for row_idx in range(rows):
    for col_idx in range(cols):
        print(f"{chr(start_idx + row_idx)}{chr(start_idx + row_idx + col_idx)}{chr(start_idx + row_idx)}",end=' ')
    print()