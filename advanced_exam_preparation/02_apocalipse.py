from collections import deque

textiles = deque(int(x) for x in input().split(" "))
medicaments = deque(int(x) for x in input().split(" "))

table_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}


created_healing_items = {}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    result = current_textile + current_medicament

    if result in table_items:
        if table_items[result] not in created_healing_items:
            created_healing_items[table_items[result]] = 0
        created_healing_items[table_items[result]] += 1

    elif result > 100:
        if "MedKit" not in created_healing_items:
            created_healing_items["MedKit"] = 0
        created_healing_items["MedKit"] += 1
        remaining_sum = result - 100
        medicaments[-1] += remaining_sum
    else: # cant create anything
        current_medicament += 10
        medicaments.append(current_medicament)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

created_healing_items = dict(sorted(created_healing_items.items(), key=lambda x: (-x[1], x[0])))

for name, amount in created_healing_items.items():
    print(f"{name} - {amount}")

if medicaments and textiles:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)[::-1]}")
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
elif medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")
elif textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")