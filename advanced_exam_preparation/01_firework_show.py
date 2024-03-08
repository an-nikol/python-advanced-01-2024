from collections import deque

firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = deque(int(x) for x in input().split(", "))

prepared_fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

has_made_fireworks = False

while True:
    if all(value >= 3 for value in prepared_fireworks.values()):
        has_made_fireworks = True
        break
    elif not firework_effects or not explosive_power:
        break

    curr_effect = firework_effects.popleft()
    curr_power = explosive_power.pop()

    if curr_effect <= 0 and curr_power <= 0:
        continue
    elif curr_effect <= 0:
        explosive_power.append(curr_power)
        continue
    elif curr_power <= 0:
        firework_effects.appendleft(curr_effect)
        continue


    result = curr_effect + curr_power

    if result % 3 == 0 and result % 5 != 0:
        prepared_fireworks["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        prepared_fireworks["Willow Fireworks"] += 1
    elif result % 3 == 0 and result % 5 == 0:
        prepared_fireworks["Crossette Fireworks"] += 1
    else:
        curr_effect -= 1
        firework_effects.append(curr_effect)
        explosive_power.append(curr_power)

if has_made_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for key, value in prepared_fireworks.items():
    print(f"{key}: {value}")