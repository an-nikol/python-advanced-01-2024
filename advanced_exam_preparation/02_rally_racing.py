n = int(input())
racing_number = input()

matrix = []
tunnels_coordinates = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "T":
            tunnels_coordinates.append([row, col])


my_position = [0, 0]

km_passed = 0
# one position - 10 kms
# if through tunnel - 30 kms

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    my_position = [my_position[0] + directions[command][0],
                   my_position[1] + directions[command][1]
    ]

    if matrix[my_position[0]][my_position[1]] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        matrix[my_position[0]][my_position[1]] = "."
        km_passed += 10
        break
    elif matrix[my_position[0]][my_position[1]] == "T":
        # remove the coordinate of the tunnel that I am on
        matrix[my_position[0]][my_position[1]] = "."
        for coordinate in tunnels_coordinates:
            if coordinate[0] == my_position[0] and coordinate[1] == my_position[1]:
                del coordinate
            else:
                my_position = [coordinate[0], coordinate[1]]
                matrix[my_position[0]][my_position[1]] = "."
        km_passed += 30
    else:
        # if he drives on a dot(free space)
        km_passed += 10


print(f"Distance covered {km_passed} km.")
matrix[my_position[0]][my_position[1]] = "C"
[print(*row, sep='') for row in matrix]
