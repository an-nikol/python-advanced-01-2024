class ValueError(Exception):
    pass


for num in range(5):
    current_num = int(input())

    if current_num < 0:
        raise ValueError("Value cannot be negative")
