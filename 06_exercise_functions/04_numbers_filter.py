def is_even(x): return x % 2 == 0
def is_odd(x): return x % 2 != 0


def even_odd_filter(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        if key not in new_dict:
            if key == "odd":
                new_dict[key] = list(filter(is_odd, value))
            elif key == "even":
                new_dict[key] = list(filter(is_even, value))

    new_dict = dict(sorted(new_dict.items(), key=lambda kvp: -len(kvp[1])))

    return new_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


