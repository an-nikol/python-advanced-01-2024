import os

path = os.path.join("..", "other", "numbers.txt")

total = 0
with open(path) as file:
    for line in file.readlines():
        total += int(line.strip())

print(total)
