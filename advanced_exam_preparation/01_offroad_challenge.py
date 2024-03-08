from collections import deque

initial_fuel = deque(int(x) for x in input().split())
additional_consumption = deque(int(x) for x in input().split())
necessary_fuel = deque(int(x) for x in input().split())

reached_altitudes = []

n = 1
while initial_fuel:

    last_fuel = initial_fuel[-1]
    first_add_cons = additional_consumption[0]

    result = last_fuel - first_add_cons

    if result >= necessary_fuel[0]:
        initial_fuel.pop()
        additional_consumption.popleft()
        necessary_fuel.popleft()
        reached_altitudes.append(f"Altitude {n}")
        print(f"John has reached: Altitude {n}")

    else:
        print(f"John did not reach: Altitude {n}")
        break

    n += 1


if initial_fuel and reached_altitudes:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached_altitudes)}")
elif initial_fuel and not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
elif not initial_fuel:
    print("John has reached all the altitudes and managed to reach the top!")
