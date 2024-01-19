from collections import deque


expression = input().split()
numbers = deque()


for char in expression:
    if char not in '*/-+':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if char == '*':
                numbers.appendleft(first_num * second_num)
            elif char == '/':
                numbers.appendleft(first_num // second_num)
            elif char == '+':
                numbers.appendleft(first_num + second_num)
            elif char == '-':
                numbers.appendleft(first_num - second_num)
print(numbers[0])





# from math import floor
#
# from collections import deque
#
# expression = deque(input().split())
#
# # for the slicing
# last_idx = 0
#
# while last_idx < len(expression):
#     # number or operator
#     element = expression[last_idx]
#
#     # if it is a number we don't do anything
#
#     if element == '*':
#         # idx - 1 is to get the numbers before the operation
#         for i in range(last_idx - 1):
#             expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
#     elif element == '/':
#         for i in range(last_idx - 1):
#             expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
#     elif element == '+':
#         for i in range(last_idx - 1):
#             expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#     elif element == '-':
#         for i in range(last_idx - 1):
#             expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
#
#     if element in '*/+-':
#         # the sum [18, *]
#         del expression[1]
#         # reset the idx
#         # 1 because 1 there is always a number
#         last_idx = 1
#
#     last_idx += 1
#
# print(floor(int(expression[0])))