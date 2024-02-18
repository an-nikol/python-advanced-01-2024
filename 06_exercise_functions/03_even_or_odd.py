def is_even(x): return x % 2 == 0
def is_odd(x): return x % 2 != 0


def even_odd(*args):
    command = args[-1]
    if command == "even":
        return list(filter(is_even, args[:-1]))
    elif command == "odd":
        return list(filter(is_odd, args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))


# def even_odd(*args):
#     command = args[-1]
#     even_numbers = []
#     odd_numbers = []
#
#     for num in args[:-1]:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#
#     if command == "even":
#         return even_numbers
#     elif command == "odd":
#         return odd_numbers