data_length = [int(i) for i in input().split()]

first_length = data_length[0]
second_length = data_length[1]

first_set = set()
second_set = set()

for i in range(1, (first_length + second_length) + 1):
    curr_num = int(input())
    if i <= first_length:
        first_set.add(curr_num)
    else:
        second_set.add(curr_num)

common_nums = first_set.intersection(second_set)
print(*common_nums, sep='\n')