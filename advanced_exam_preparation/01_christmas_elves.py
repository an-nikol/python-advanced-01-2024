from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials_boxes = deque(int(x) for x in input().split())

total_created_toys = 0
total_used_energy = 0
iterations = 0

while elves_energy and materials_boxes:
    current_elf_energy = elves_energy.popleft()
    current_box = materials_boxes[-1]
    recently_added_toys = 0

    # takes a day off
    if current_elf_energy < 5:
        continue

    # adds an iteration
    iterations += 1

    # check if this is a third iteration(out of the below check, because the value of the box is elavated.
    if iterations % 3 == 0:
        current_box *= 2
        recently_added_toys += 1

    # the main point in the task. If the elf can crate a toy.
    if current_elf_energy >= current_box:
        total_used_energy += current_box
        current_elf_energy -= current_box

        # check if a toy will be added and cookie received
        if iterations % 5 != 0:
            current_elf_energy += 1
            recently_added_toys += 1
        else: # on fifth iteration
            recently_added_toys = 0

        materials_boxes.pop()
        # when the elf does not have enough energy he does not make a toy.
    else:
        current_elf_energy *= 2
        recently_added_toys = 0

    # add all toys from current iteration
    total_created_toys += recently_added_toys

    elves_energy.append(current_elf_energy)

print(f"Toys: {total_created_toys}")
print(f"Energy: {total_used_energy}")

if elves_energy and materials_boxes:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
    print(f"Boxes left: {', '.join([str(x) for x in materials_boxes])}")
elif elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
elif materials_boxes:
    print(f"Boxes left: {', '.join([str(x) for x in materials_boxes])}")
