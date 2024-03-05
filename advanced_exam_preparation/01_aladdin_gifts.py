from collections import deque


def create_presents(res):
    if 100 <= res <= 199:
        crafted_presents["Gemstone"] += 1
    elif 200 <= res <= 299:
        crafted_presents["Porcelain Sculpture"] += 1
    elif 300 <= res <= 399:
        crafted_presents["Gold"] += 1
    elif 400 <= res <= 499:
        crafted_presents["Diamond Jewellery"] += 1
    else:
        return False


materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

crafted_presents = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    result = current_material + current_magic
    made_present = create_presents(result)

    if not made_present:
        if result < 100:
            if result % 2 == 0:
                current_material *= 2
                current_magic *= 3
                curr_result = current_material + current_magic
                create_presents(curr_result)
            else:
                result *= 2
                create_presents(result)
        elif result > 499:
            result /= 2
            create_presents(result)

if (crafted_presents["Gemstone"] >= 1 and crafted_presents["Porcelain Sculpture"] >= 1) or \
        (crafted_presents["Gold"] >= 1 and crafted_presents["Diamond Jewellery"] >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

crafted_presents = dict(sorted(crafted_presents.items(), key=lambda x:x[0]))

for key, value in crafted_presents.items():
    if value:
        print(f"{key}: {value}")