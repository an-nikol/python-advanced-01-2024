def is_out_the_board(r, c):
    return 0 > r or r >= n or 0 > c or c >= n


n = int(input())

matrix = []
my_position = []

money = 100

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "G":
            my_position = [row, col]
            matrix[row][col] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
is_game_over = False
has_won_jackpot = False

while True:
    command = input()
    if command == "end":
        break

    # moved gambler
    my_position = [my_position[0] + directions[command][0], my_position[1] + directions[command][1]]

    # check if he is in the board
    if is_out_the_board(my_position[0], my_position[1]) or money <= 0:
        is_game_over = True
        money = 0
        print("Game over! You lost everything!")
        break

    if matrix[my_position[0]][my_position[1]] == "W":
        matrix[my_position[0]][my_position[1]] = "-"
        money += 100

    elif matrix[my_position[0]][my_position[1]] == "P":
        matrix[my_position[0]][my_position[1]] = "-"
        money -= 200

        if money <= 0:
            money = 0
            is_game_over = True
            print("Game over! You lost everything!")
            break

    elif matrix[my_position[0]][my_position[1]] == "J":
        has_won_jackpot = True
        matrix[my_position[0]][my_position[1]] = "-"
        money += 100000
        break

matrix[my_position[0]][my_position[1]] = "G"

if not is_game_over:
    if has_won_jackpot:
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
    else:
        print(f"End of the game. Total amount: {money}$")

if money:
    [print(*row, sep='') for row in matrix]
