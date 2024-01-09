from collections import deque

text = input()
my_stack = deque(text)


for char in text:
    my_stack.appendleft(char)
    my_stack.pop()

print(f"{''.join(my_stack)}")