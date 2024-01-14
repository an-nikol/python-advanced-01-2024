from collections import deque

clothes = deque([int(n) for n in input().split()])
capacity_of_one_rack = int(input())
number_of_rakes = 1
current_free_space = capacity_of_one_rack
# use a stack

while clothes:
    piece_of_clothing = clothes.pop()
    # if the space is bigger than the clothing
    if current_free_space >= piece_of_clothing:
        current_free_space -= piece_of_clothing
    else:
        number_of_rakes += 1
        # we have already got one piece of clothing
        current_free_space = capacity_of_one_rack - piece_of_clothing

print(number_of_rakes)