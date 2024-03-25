def start_spring(**kwargs):
    some_dict = {}
    result = ""
    for curr_name, curr_type in kwargs.items():
        if curr_type not in some_dict:
            some_dict[curr_type] = []
        some_dict[curr_type].append(curr_name)

    some_dict = dict(sorted(some_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    for curr_type, names in some_dict.items():
        result += f"{curr_type}:\n"
        sorted_names = sorted(names)
        for name in sorted_names:
            result += f"-{name}\n"

    return result



example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
