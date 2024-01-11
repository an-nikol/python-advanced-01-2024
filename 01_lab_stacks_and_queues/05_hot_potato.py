from collections import deque

names = deque(input().split())
rotation = int(input()) - 1

while len(names) > 1:
    names.rotate(-rotation)
    exited_name = names.popleft()
    print(f'Removed {exited_name}')

print(f"Last is {names.popleft()}")





#print(f'Removed {my_queue[final_toss]}')


#print(my_queue)
