n = int(input())

matrix = []
alice_position = [0, 0]


for r in range(n):
    matrix.append([symbol for symbol in input().split()])
    for c in range(n):
        if matrix[r][c] == 'A':
            alice_position = r, c
            matrix[r][c] = "*"

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


tea_bags = 0

while True:
    command = input()
    if command in direction:

        new_row = alice_position[0] + direction[command][0]
        new_col = alice_position[1] + direction[command][1]

        if 0 > new_row or new_row >= n or 0 > new_col or new_col >= n:
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[new_row][new_col] == "R":
            print("Alice didn't make it to the tea party.")
            matrix[new_row][new_col] = "*"
            break
        else:
            # collect tea bags
            if matrix[new_row][new_col] not in ".*":
                tea_bags += int(matrix[new_row][new_col])
                matrix[new_row][new_col] = "*"
                # move alice
                alice_position = new_row, new_col

                if tea_bags >= 10:
                    print("She did it! She went to the party.")
                    break
            else: # if she steps on an empty spot
                # move alice
                alice_position = new_row, new_col
                matrix[new_row][new_col] = "*"

[print(*row, sep=' ') for row in matrix]