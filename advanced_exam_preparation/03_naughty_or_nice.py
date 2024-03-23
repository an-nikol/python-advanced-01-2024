def naughty_or_nice_list(kids: list, *commands, **kwargs):
    #  create the three lists that will be returned as a result
    naughty_list = []
    nice_list = []
    not_found_list = []
    result = ""

    # Step 1. Start iterating over the commands
    for command in commands:
        # NB! Save all the nums from the kids in a list
        nums_from_kids = [int(x[0]) for x in kids]
        num, behaviour = command.split('-')
        num = int(num)
        # NB! Check if there is more than one occur of the number in the list
        if nums_from_kids.count(num) > 1:
            continue

        # Step 2. Fill the appropriate lists with the info from the list
        for curr_tuple in kids:
            code, name = curr_tuple
            if num == curr_tuple[0]:
                if behaviour == 'Nice':
                    nice_list.append(name)
                    kids.remove(curr_tuple)
                elif behaviour == 'Naughty':
                    naughty_list.append(name)
                    kids.remove(curr_tuple)

    # Step 3. Start iterating over the dictionary.
    for key, value in kwargs.items():
        # NB! Store all the nums from kids list.
        reference_list_name = [x[1] for x in kids]
        # NB! Check if the occur are more than 1
        if reference_list_name.count(key) > 1:
            continue

        # Step 4. Fill the appropriate lists with the info from the dictionary.
        for curr_tuple in kids:
            num, name = curr_tuple
            if key == name:
                if value == 'Nice':
                    nice_list.append(name)
                    kids.remove(curr_tuple)
                elif value == 'Naughty':
                    naughty_list.append(name)
                    kids.remove(curr_tuple)

    # Step 5. Fill the remaining items of Santa's list as not found kids.
    for curr_tuple in kids:
        not_found_list.append(curr_tuple[1])

    # Step 6. Add the information to result and return it
    if nice_list:
        result += f"Nice: {', '.join(nice_list)}" + '\n'
    if naughty_list:
        result += f"Naughty: {', '.join(naughty_list)}" + '\n'
    if not_found_list:
        result += f"Not found: {', '.join(not_found_list)}"

    return result


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
