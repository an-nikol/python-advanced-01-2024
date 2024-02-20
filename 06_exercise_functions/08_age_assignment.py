def age_assignment(*args, **kwargs):
    new_dict = {}

    for name in args:
        for char, years in kwargs.items():
            if name[0] == char:
                new_dict[name] = years

    sorted_dict = dict(sorted(new_dict.items(), key=lambda x: x[0]))

    return "\n".join(f"{name} is {age} years old." for name, age in sorted_dict.items())



print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
