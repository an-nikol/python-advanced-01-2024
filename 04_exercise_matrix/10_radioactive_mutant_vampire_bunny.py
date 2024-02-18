def find_player_position():
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'P':
                return r, c


def check_is_valid_position(object_row, object_col, player=False):
    global has_won

    if 0 <= object_row < rows and 0 <= object_col < cols:
        return True

        # if the index is invalid and the function has not returned anything
    if player:
        has_won = True


def bunnies_positions():
    all_positions = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'B':
                all_positions.append([r, c])
    return all_positions


def spread_bunnies(list_of_bunnies_positions):
    for each_bunny_coordinate in range(len(list_of_bunnies_positions)):
        current_bunny_row, current_bunny_col = list_of_bunnies_positions[each_bunny_coordinate]
        for direction in directions.values():
            new_row = current_bunny_row + direction[0]
            new_col = current_bunny_col + direction[1]

            if check_is_valid_position(new_row, new_col):
                matrix[new_row][new_col] = "B"


def is_player_alive(row, col):
    if matrix[row][col] == "B":
        show_results("dead:")


def show_results(status="won:"):
    [print(*row, sep='') for row in matrix]
    print(f"{status} {current_player_row} {current_player_col}")

    raise SystemExit


rows, cols = [int(num) for num in input().split()]

matrix = [list(input()) for r in range(rows)]

commands = input()

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

has_won = False

current_player_row, current_player_col = find_player_position()
matrix[current_player_row][current_player_col] = '.'

for command in commands:
    player_next_row = current_player_row + directions[command][0]
    player_next_col = current_player_col + directions[command][1]

    # before moving him check if he has won or died
    if check_is_valid_position(player_next_row, player_next_col, True):
        current_player_row = player_next_row
        current_player_col = player_next_col

    positions_of_bunnies = bunnies_positions()

    spread_bunnies(positions_of_bunnies)

    if has_won:
        show_results()

    is_player_alive(current_player_row, current_player_col)
