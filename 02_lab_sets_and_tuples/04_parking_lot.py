number_of_commands = int(input())\

parking = set()

for i in range(number_of_commands):
    direction, number = input().split(', ')
    if direction == 'IN':
        parking.add(number)
    elif direction == 'OUT':
        if number in parking:
            parking.remove(number)

if parking:
    print(*parking, sep='\n')
else:
    print('Parking Lot is Empty')
