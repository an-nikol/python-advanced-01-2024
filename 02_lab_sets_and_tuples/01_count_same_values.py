numbers = tuple([float(num) for num in input().split()])

my_dict = {}

for num in numbers:
    if num not in my_dict:
        my_dict[num] = 0
    my_dict[num] += 1

for key, value in my_dict.items():
    print(f'{key} - {value} times')

