from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees = deque(int(x) for x in input().split(", "))

total_pizzas = 0

while pizza_orders and employees:
    current_pizza_order = pizza_orders.popleft()
    if current_pizza_order <= 0:
        continue

    current_employee = employees.pop()

    if current_pizza_order > 10:
        employees.append(current_employee)
        continue

    if current_pizza_order > current_employee:
        total_pizzas += current_employee
        current_pizza_order -= current_employee
        pizza_orders.appendleft(current_pizza_order)
    else:
        total_pizzas += current_pizza_order

if not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")

elif not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")

