user_input = input().split()

num_1 = float(user_input[0])
sign = user_input[1]
num_2 = int(user_input[2])

mapper = {
    "/": num_1 / num_2,
    "*": num_1 * num_2,
    "-": num_1 - num_2,
    "+": num_1 + num_2,
    "^": num_1**num_2
}

print(f"{mapper[sign]:.2f}")

