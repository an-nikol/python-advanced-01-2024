txt = input()
times = input()

try:
    result = txt * int(times)
    print(result)
except ValueError:
    print("Variable times must be an integer")