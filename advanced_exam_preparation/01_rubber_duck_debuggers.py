from collections import deque

time_to_solve_task = deque(int(x) for x in input().split())
number_of_tasks = deque(int(x) for x in input().split())

dict_type_count = {"Darth Vader Ducky":0,"Thor Ducky":0, "Big Blue Rubber Ducky":0, "Small Yellow Rubber Ducky": 0 }

while time_to_solve_task and number_of_tasks:
    current_time = time_to_solve_task.popleft()
    current_num_tasks = number_of_tasks.pop()

    result = current_time * current_num_tasks

    if 0 <= result <= 60:
        dict_type_count["Darth Vader Ducky"] += 1

    elif 61 <= result <= 120:
        dict_type_count["Thor Ducky"] += 1

    elif 121 <= result <= 180:
        dict_type_count["Big Blue Rubber Ducky"] += 1

    elif 181 <= result <= 240:
        dict_type_count["Small Yellow Rubber Ducky"] += 1

    else:
        number_of_tasks.append(current_num_tasks - 2)
        time_to_solve_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for type, count in dict_type_count.items():
    print(f"{type}: {count}")
