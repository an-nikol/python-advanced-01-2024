def fill_the_box(height, length, width, *args):
    free_space = height * length * width
    all_cubes = 0

    for num in args:
        if num == "Finish":
            break
        all_cubes += num

    if all_cubes > free_space:
        return f"No more free space! You have {all_cubes - free_space} more cubes."

    elif all_cubes <= free_space:
        return f"There is free space in the box. You could put {free_space - all_cubes} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
