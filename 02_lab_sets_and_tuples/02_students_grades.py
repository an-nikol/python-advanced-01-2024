number_of_students = int(input())

students = {}


for student in range(number_of_students):
    name, grade = tuple(input().split())
    grade = (float(grade))

    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    avg = sum(grades) / len(grades)

    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades ])} (avg: {avg:.2f})")