from collections import deque

from datetime import datetime, timedelta
# datetime gives us methods, timedelta = adding time

robots = {}

for robot in input().split(","):
    name, time_needed = robot.split("-")
    robots[name] = [int(time_needed), 0]

# object time, not a normal string
factory_time = datetime.strptime(input(), "%H: %M:%S")
products = deque()

while True:
    product = input()
    if product == 'End':
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = product.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
