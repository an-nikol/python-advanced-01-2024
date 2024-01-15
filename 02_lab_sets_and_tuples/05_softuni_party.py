number_of_guests = int(input())

reservations = set()

for i in range(number_of_guests):
    code = input()
    reservations.add(code)

guests_that_came = set()

guest_that_came = input()
while guest_that_came != 'END':
    guests_that_came.add(guest_that_came)
    guest_that_came = input()

guests_that_did_not_come = reservations.difference(guests_that_came)
print(len(guests_that_did_not_come))

guests_that_did_not_come = sorted(guests_that_did_not_come)

print(*guests_that_did_not_come, sep='\n')