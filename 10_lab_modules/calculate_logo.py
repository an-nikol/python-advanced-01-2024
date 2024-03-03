from math import log

n = int(input())
base = input()

try:
    print(f"{log(n, int(base)):.2f}")
except ValueError:
    print(f"{log(n):.2f}")