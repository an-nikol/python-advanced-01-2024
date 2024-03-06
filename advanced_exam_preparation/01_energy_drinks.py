from collections import deque

caffeine_mgs = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

current_caffeine = 0

while caffeine_mgs and energy_drinks:
    current_caffeine_mlg = caffeine_mgs.pop()
    current_energy_drink = energy_drinks.popleft()

    result = current_caffeine_mlg * current_energy_drink

    if current_caffeine + result <= 300:
        current_caffeine += result
    else:
        energy_drinks.append(current_energy_drink)
        current_caffeine -= 30
        if current_caffeine <= 0:
            current_caffeine = 0


if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")