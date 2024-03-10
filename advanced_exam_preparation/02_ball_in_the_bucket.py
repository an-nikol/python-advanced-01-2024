def invalid_idx(r, c):
    return 0 > r or r >= n or 0 > c or c >= n


n = 6

matrix = [[col for col in input().split()] for row in range(n)]

scored_points = 0

throws = 3

for throw in range(throws):
    curr_coordinates = [int(x) for x in input()[1:-1].split(", ")]
    if invalid_idx(curr_coordinates[0], curr_coordinates[1]):
        continue
    elif matrix[curr_coordinates[0]][curr_coordinates[1]] == "B":
        matrix[curr_coordinates[0]][curr_coordinates[1]] = "0"
        for row in range(n):
            scored_points += int(matrix[row][curr_coordinates[1]])

if scored_points >= 300:
    print(f"Good job! You scored {scored_points} points, and you've won Lego Construction Set.")
elif 200 <= scored_points <= 299:
    print(f"Good job! You scored {scored_points} points, and you've won Teddy Bear.")
elif 100 <= scored_points <= 199:
    print(f"Good job! You scored {scored_points} points, and you've won Football.")
else:
    print(f"Sorry! You need {100 - scored_points} points more to win a prize.")
