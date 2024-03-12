from collections import deque


def is_invalid_index(r, c):
    return 0 > r or r >= n or 0 > c or c >= n


n = 7

player_names = deque(input().split(", "))

points_board = {}

for player_name in player_names:
    if player_name not in points_board:
        points_board[player_name] = 501

count_turns = {}
for player_name in player_names:
    if player_name not in count_turns:
        count_turns[player_name] = 0

matrix = [[col for col in input().split()] for row in range(n)]

while True:
    curr_coordinate = [int(x) for x in input()[1:-1].split(", ")]
    curr_name = player_names[0]
    count_turns[curr_name] += 1
    player_names.rotate(-1)

    if is_invalid_index(curr_coordinate[0], curr_coordinate[1]):
        continue
    elif matrix[curr_coordinate[0]][curr_coordinate[1]] == "D":
        curr_sum = (int(matrix[0][curr_coordinate[1]]) + int(matrix[n - 1][curr_coordinate[1]])\
                    + int(matrix[curr_coordinate[0]][0]) + int(matrix[curr_coordinate[0]][n - 1])) * 2

        points_board[curr_name] -= curr_sum
    elif matrix[curr_coordinate[0]][curr_coordinate[1]] == "T":
        curr_sum = (int(matrix[0][curr_coordinate[1]]) + int(matrix[n - 1][curr_coordinate[1]]) \
                    + int(matrix[curr_coordinate[0]][0]) + int(matrix[curr_coordinate[0]][n - 1])) * 3

        points_board[curr_name] -= curr_sum
    elif matrix[curr_coordinate[0]][curr_coordinate[1]] == "B":
        print(f"{curr_name} won the game with {count_turns[curr_name]} throws!") # fix the throws to work with 1
        break
    else:
        points_board[curr_name] -= int(matrix[curr_coordinate[0]][curr_coordinate[1]])

    if any([True for k, v in points_board.items() if v <= 0]):
        print(f"{curr_name} won the game with {count_turns[curr_name]} throws!")
        break
