n = int(input())

battle_cruisers = 3
hits_from_mines = 0
submarine_position = []
matrix = []

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "S":
            submarine_position = [row, col]
            matrix[row][col] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while battle_cruisers != 0 and hits_from_mines != 3:
    command = input()

    submarine_position = [
        submarine_position[0] + directions[command][0],
        submarine_position[1] + directions[command][1]
    ]

    if matrix[submarine_position[0]][submarine_position[1]] == "*":
        matrix[submarine_position[0]][submarine_position[1]] = "-"
        hits_from_mines += 1
    elif matrix[submarine_position[0]][submarine_position[1]] == "C":
        matrix[submarine_position[0]][submarine_position[1]] = "-"
        battle_cruisers -= 1

matrix[submarine_position[0]][submarine_position[1]] = "S"

if battle_cruisers == 0:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

if hits_from_mines == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")

[print(*row, sep="") for row in matrix]