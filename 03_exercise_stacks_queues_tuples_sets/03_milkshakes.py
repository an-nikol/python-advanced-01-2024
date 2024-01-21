from collections import deque

chocolates = deque([int(num) for num in input().split(', ')])
cups_of_milk = deque([int(num) for num in input().split(', ')])


milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    last_chocolate = chocolates.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    # edge case
    if last_chocolate <= 0 and current_cup_of_milk <= 0:
        continue
    elif last_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_of_milk)
        continue
    elif current_cup_of_milk <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == current_cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(current_cup_of_milk)
        chocolates.append(last_chocolate - 5)

if milkshakes >= 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")

from collections import deque

chocolates = deque(int(x)for x in input().split(', '))
cups_of_milk = deque(int(x)for x in input().split(', '))

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    last_chocolate = chocolates[-1]
    first_cup_of_milk = cups_of_milk[0]

    if last_chocolate <= 0 and first_cup_of_milk <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    if last_chocolate <= 0:
        chocolates.pop()
        continue
    if first_cup_of_milk <= 0:
        cups_of_milk.popleft()
        continue

    if last_chocolate == first_cup_of_milk:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.popleft()
        cups_of_milk.append(first_cup_of_milk)
        chocolates[-1] -= 5


if milkshakes >= 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
print(f"Chocolate: {', '.join([str(i) for i in chocolates]) if chocolates else 'empty'}")
print(f"Milk: {', '.join([str(i) for i in cups_of_milk]) if cups_of_milk else 'empty'}")



# from collections import deque
#
# chocolates = deque(int(x)for x in input().split(', '))
# cups_of_milk = deque(int(x)for x in input().split(', '))
#
# milkshakes = 0
#
# while milkshakes < 5 and chocolates and cups_of_milk:
#     last_chocolate = chocolates[-1]
#     first_cup_of_milk = cups_of_milk[0]
#
#     if last_chocolate <= 0 and first_cup_of_milk <= 0:
#         chocolates.pop()
#         cups_of_milk.popleft()
#         continue
#     if last_chocolate <= 0:
#         chocolates.pop()
#         continue
#     if first_cup_of_milk <= 0:
#         cups_of_milk.popleft()
#         continue
#
#     if last_chocolate == first_cup_of_milk:
#         chocolates.pop()
#         cups_of_milk.popleft()
#         milkshakes += 1
#     else:
#         cups_of_milk.popleft()
#         cups_of_milk.append(first_cup_of_milk)
#         chocolates[-1] -= 5
#
#
# if milkshakes >= 5:
#     print('Great! You made all the chocolate milkshakes needed!')
# else:
#     print('Not enough milkshakes.')
# print(f"Chocolate: {', '.join([str(i) for i in chocolates]) if chocolates else 'empty'}")
# print(f"Milk: {', '.join([str(i) for i in cups_of_milk]) if cups_of_milk else 'empty'}")
