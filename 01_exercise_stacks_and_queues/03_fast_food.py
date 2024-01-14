from collections import deque

qty_food = int(input())
# orders in a Q
orders = deque([int(n) for n in input().split()])

# find the biggest order and print it
print(max(orders))

# servicing the clients

for order in orders.copy():
    # before each order check if you have enough food
    if qty_food - order >= 0:
        orders.popleft()
        qty_food -= order
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
# if this cycle is not breaked
else:
    print('Orders complete')
