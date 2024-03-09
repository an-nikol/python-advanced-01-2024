from collections import deque

worms = deque([int(x) for x in input().split()])
holes = deque([int(x) for x in input().split()])

matches_counter = 0
all_worms_fit_a_hole = True

while worms and holes:
    last_worm = worms[-1]
    first_hole = holes[0]

    if last_worm == first_hole:
        worms.pop()
        holes.popleft()
        matches_counter += 1

    else:
        holes.popleft()
        all_worms_fit_a_hole = False
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matches_counter:
    print(f"Matches: {matches_counter}")
else:
    print("There are no matches.")

if not worms and all_worms_fit_a_hole:
    print("Every worm found a suitable hole!")
elif not worms and not all_worms_fit_a_hole:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
