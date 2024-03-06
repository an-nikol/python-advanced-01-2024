from collections import deque

food_portions = deque(int(x) for x in input().split(", "))
stamina_portions = deque(int(x) for x in input().split(", "))
climbed_peaks = []
days = 1

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

while True:
    if len(climbed_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

    if days > 7 or not food_portions or not stamina_portions:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    current_food = food_portions.pop()
    current_stamina = stamina_portions.popleft()
    current_peak = peaks.popleft()
    result = current_food + current_stamina
    if result >= current_peak[1]:
        climbed_peaks.append(current_peak[0])
        days += 1
    else:
        peaks.appendleft(current_peak)
        days += 1


if climbed_peaks:
    print(f"Conquered peaks:")
    print(*climbed_peaks, sep="\n")

