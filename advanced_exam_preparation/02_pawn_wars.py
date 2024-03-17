# 1. Find positions of the white and black pawns

# 2. First case (not neighboring positions)
# 1) Check if the two pawns are NOT in neighboring columns. Particularly, /
# check if the cols DO NOT have 1 col diff (abs).
# 2) If the two pawns are NOT neighboring - find which pawn will reach the end first. This is found by moving the
# white pawn in its mirroring position on the side of the black pawn to check which idx is bigger (which will win).
# The formula for this is n - white_pos_row - 1 > n - black_pos_row. (-1 is due to len and idx diff)

# 3. ELSE: Second case (if the pawns are IN neighboring positions)
# 1) Check if the two pawns start at the SAME even/odd position. (e. g. even row-even row/ odd row - odd row).
# If the pawns are in the same position - BLACK takes. Otherwise, WHITE takes.

# 4. Find the place where the pawns take each other
# Usually the pawn will meet in the middle. But a bit specific where exactly it is in the middle.
# 1) the formula for finding the position where they meet: (white row_idx + black row_idx) // 2

# 5. Printing the exact squire (a4, b8, etc)
# 1) if the pawns are in neighboring positions (First case)
# - find the letter and number -
# chr 97 + black pos // chr 97 + white pos (the white/black row_idx and col_idx where the white/black pawn finished)
# 2) if the pawns are in neighboring positions(Second case)
# REMARK: the black takes on the WHITE col. Similarly, the white takes on the BLACK col.
# - find the letter
# the formula for finding the letters is chr(97 + pos[white_row_idx][black_col_idx] //
# 97 + pos[black_row_idx][white_row_idx]
# - find the num (because the boarding numbering is different than the programming way to find the num
# the formula is n - place(point 4.)

n = 8

matrix = []

white_pos = []
black_pos = []


for row in range(8):
    matrix.append(input().split())
    for col in range(8):
        if matrix[row][col] == "w":
            white_pos = [row, col]
        elif matrix[row][col] == "b":
            black_pos = [row, col]

# first case: check if the two pawns are NOT neighboring cols
if abs(white_pos[1] - black_pos[1]) != 1:
    # find which pawn will reach the end first
    if n - white_pos[0] - 1 <= black_pos[0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_pos[1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_pos[1])}8.")

# second case: check if the two pawns are IN neighbouring positions
else:
    place = (white_pos[0] + black_pos[0]) // 2

    if white_pos[0] % 2 == black_pos[0] % 2: # same position odd-odd / even-even
        print(f"Game over! Black win, capture on {chr(97 + white_pos[1])}{n - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + black_pos[1])}{n - place}.")

# from math import ceil
#
# size = 8
# matrix = []
# white_row, white_col = 0, 0
# black_row, black_col = 0, 0
#
# matrix_board = []
# for board_row in range(size, 0, -1):
#     value = [f'{chr(97 + x)}{board_row}' for x in range(size)]
#     matrix_board.append(value)
#
# for row in range(size):
#     value = input().split()
#     matrix.append(value)
#     for col in range(size):
#         if matrix[row][col] == 'b':
#             black_row, black_col = row, col
#
#         elif matrix[row][col] == 'w':
#             white_row, white_col = row, col
#
# if not abs(black_col - white_col) == 1:
#     if (size - black_row) > white_row:
#         print(f"Game over! White pawn is promoted to a queen at {matrix_board[size - size][white_col]}.")
#
#     else:
#         print(f"Game over! Black pawn is promoted to a queen at {matrix_board[size - 1][black_col]}.")
#
#
# else:
#     if abs(black_row - white_row) % 2 == 0:
#         print(
#             f"Game over! Black win, capture on {matrix_board[black_row + ceil(abs(black_row - white_row) / 2)][white_col]}.")
#
#     else:
#         print(
#             f"Game over! White win, capture on {matrix_board[white_row - ceil(abs(black_row - white_row) / 2)][black_col]}.")

# def check_if_can_capture(coordinates_attacker, coordinates_defender):
#     row_a = coordinates_attacker[0]
#     col_a = coordinates_attacker[1]
#     row_d = coordinates_defender[0]
#     col_d = coordinates_defender[1]
#
#     if row_a - 1 >= 0 and col_a - 1 >= 0:
#         if row_a - 1 == row_d and col_a - 1 == col_d:
#             return [row_a - 1, col_a - 1]
#     if row_a - 1 >= 0 and col_a + 1 < 8:
#         if row_a - 1 == row_d and col_a + 1 == col_d:
#             return [row_a - 1, col_a + 1]
#     if row_a + 1 < 8 and col - 1 >= 0:
#         if row_a + 1 == row_d and col_a - 1 == col_d:
#             return [row_a + 1, col_a - 1]
#     if row_a + 1 < 8 and col + 1 < 8:
#         if row_a + 1 == row_d and col_a + 1 == col_d:
#             return [row_a + 1, col_a + 1]
#
#
# n = 8
#
# matrix = []
# white_pawn_coordinates = []
# black_pawn_coordinates = []
#
# # read the matrix and fin the positions of black and white
# for row in range(n):
#     matrix.append(input().split())
#     for col in range(n):
#         if matrix[row][col] == "w":
#             white_pawn_coordinates = [row, col]
#         if matrix[row][col] == "b":
#             black_pawn_coordinates = [row, col]
#
# # mark rows positions
# position_row = {
#     0: "8",
#     1: "7",
#     2: "6",
#     3: "5",
#     4: "4",
#     5: "3",
#     6: "2",
#     7: "1",
# }
#
# # mark cols positions
# positions_col = {
#     0: "a",
#     1: "b",
#     2: "c",
#     3: "d",
#     4: "e",
#     5: "f",
#     6: "g",
#     7: "h",
# }
#
# for _ in range(8):
#     # check if a pawn can capture the other one
#     capture_on = check_if_can_capture(white_pawn_coordinates, black_pawn_coordinates)
#
#     if capture_on:
#         position = positions_col[capture_on[1]] + position_row[capture_on[0]]
#         print(f"Game over! White win, capture on {position}.")
#         break
#
#     white_pawn_coordinates[0] -= 1
#
#     if white_pawn_coordinates[0] == 0:
#         position = positions_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
#         print(f"Game over! White pawn is promoted to a queen at {position}.")
#         break
#
#     capture_on = check_if_can_capture(black_pawn_coordinates, white_pawn_coordinates)
#     if capture_on:
#         position = positions_col[capture_on[1]] + position_row[capture_on[0]]
#         print(f"Game over! Black win, capture on {position}.")
#         break
#
#     black_pawn_coordinates[0] += 1
#
#     if black_pawn_coordinates[0] == 7:
#         position = positions_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
#         print(f"Game over! Black pawn is promoted to a queen at {position}.")
#         break
