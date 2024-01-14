text = input()

my_dict = {}

for char in text:
    if char not in my_dict:
        my_dict[char] = 0
    my_dict[char] += 1

sorted_dict = dict(sorted(my_dict.items()))

for key, value in sorted_dict.items():
    print(f'{key}: {value} time/s')