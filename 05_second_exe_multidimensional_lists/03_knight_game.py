n = int(input())

matrix = []

knights_positions = []

for row in range(n):
    matrix.append([symbol for symbol in input()])
    for col in range(n):
        if matrix[row][col] == "K":
            knights_positions.append([row, col])

possible_attacks = (
    (-2, 1),
    (-1, 2),
    (-2, -1),
    (-1, -2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2)
)

removed_knights = 0

while True:     # continues while there are no knights attacking other knights
    max_attacks = 0
    max_knight = [0, 0]
    for k_row, k_col in knights_positions:
        current_hits = 0
        for attack in possible_attacks:

            new_row, new_col = attack[0], attack[1]

            attacked_row = k_row + new_row
            attacked_col = k_col + new_col

            # check if idx is valid
            if 0 <= attacked_row < n and 0 <= attacked_col < n:
                if matrix[attacked_row][attacked_col] == 'K':
                    current_hits += 1

        # here we check to get the top left knight
        if current_hits > max_attacks:
            max_attacks = current_hits
            max_knight = [k_row, k_col]

    # situations to exit the program
    if max_attacks == 0:
        break
    knights_positions.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)
