from collections import deque
eggs = deque(int(x) for x in input().split(", "))
pieces_of_paper = deque(int(x) for x in input().split(", "))

BOX_SIZE = 50

BAD_LUCK_EGG = 13

filled_boxes = 0

while eggs and pieces_of_paper:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    elif current_egg == BAD_LUCK_EGG:
        first_egg = pieces_of_paper.popleft()
        last_egg = pieces_of_paper.pop()
        pieces_of_paper.append(first_egg)
        pieces_of_paper.appendleft(last_egg)
        continue

    current_piece_of_paper = pieces_of_paper.pop()

    if current_egg + current_piece_of_paper <= BOX_SIZE:
        filled_boxes += 1


if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs and pieces_of_paper:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
    print(f"Pieces of paper left: {', '.join([str(x) for x in pieces_of_paper])}")
elif eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
elif pieces_of_paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in pieces_of_paper])}")