first_set = set([int(n) for n in input().split()])
second_set = set([int(j) for j in input().split()])

number_of_commands = int(input())

for i in range(number_of_commands):
    first_command, second_command, *data = input().split() # Add First 5 6 9 3 => ["Add", "First", ['5', '6', '9', '3']

    command = first_command + ' ' + second_command

    if command == 'Add First':
        [first_set.add(int(el))for el in data]
    elif command == 'Add Second':
        [second_set.add(int(el)) for el in data]
    elif command == 'Remove First':
        [first_set.discard(int(el)) for el in data]
    elif command == 'Remove Second':
        [second_set.discard(int(el)) for el in data]
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))


print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
