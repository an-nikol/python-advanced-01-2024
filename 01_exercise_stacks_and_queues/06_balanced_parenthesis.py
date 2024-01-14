from collections import deque

# save all parenthesis we have
all_parenthesis = deque(input()) # ['(']

# second deque for open_parenthesis
open_parenthesis = deque()

while all_parenthesis: # if its not breaked -> false -> else
    current_parenthesis = all_parenthesis.popleft()

    if current_parenthesis in "({[":
        open_parenthesis.append(current_parenthesis)
        # if it starts with a closing parenthesis - not valid
        # otherwise error because the closed parenthesis is not discussed
    elif not open_parenthesis:
        print("NO")
        break
    else:
        # compare with the last closed parenthesis
        if f"{open_parenthesis.pop() + current_parenthesis}" not in "()[]{}":
            print("NO")
            break
else:
    print('YES')

