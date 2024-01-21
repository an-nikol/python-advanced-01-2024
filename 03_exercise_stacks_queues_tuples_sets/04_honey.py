from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())


total_honey = 0

# mapper
operations = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    elif curr_nectar > curr_bee:
        total_honey += abs(operations[symbols.popleft()](curr_bee, curr_nectar))

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")




# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = deque(int(x) for x in input().split())
# operations = deque(input().split())
#
# total_honey_made = 0
#
# while bees and nectar:
#     # step 1 check if it has collected enough nectar
#     first_bee = bees[0]
#     last_nectar = nectar[-1]
#
#     if last_nectar >= first_bee:
#         curr_operation = operations.popleft()
#         if curr_operation == '+':
#             total_honey_made += abs(first_bee + last_nectar)
#             bees.popleft()
#             nectar.pop()
#         elif curr_operation == '-':
#             total_honey_made += abs(first_bee - last_nectar)
#             bees.popleft()
#             nectar.pop()
#         elif curr_operation == '*':
#             total_honey_made += abs(first_bee * last_nectar)
#             bees.popleft()
#             nectar.pop()
#         elif curr_operation == '/':
#             if last_nectar > 0:
#                 total_honey_made += abs(first_bee / last_nectar)
#                 bees.popleft()
#                 nectar.pop()
#             else:
#                 bees.popleft()
#                 nectar.pop()
#
#     elif last_nectar < first_bee:
#         nectar.pop()
#
# print(f"Total honey made: {total_honey_made}")
#
# if bees:
#     print(f"Bees left: {', '.join([str(x) for x in bees])}")
# if nectar:
#     print(f"Nectar left: {', '.join([str(x) for x in nectar])}")