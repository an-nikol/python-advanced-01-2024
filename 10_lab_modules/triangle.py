def create_triangle(n):
    for row in range(n):
        for col in range(row + 1):
            print(col + 1, end=' ')
        print()

    for row in range(n - 1, 0, -1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()


n = int(input())
create_triangle(n)
