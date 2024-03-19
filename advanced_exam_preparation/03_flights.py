def flights(*args):
    some_dict = {}
    for idx in range(0, len(args), 2):
        if args[idx] == "Finish":
            break
        elif args[idx] not in some_dict:
            some_dict[args[idx]] = args[idx + 1]
        else:
            some_dict[args[idx]] += args[idx + 1]
    return some_dict

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))