def create_seq(n):
    seq = [0, 1]

    for _ in range(n - 2):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)


    return seq


def locate_number(num, seq):
    try:
        idx = seq.index(num)
        return f"The number - {num} is at index {idx}"
    except ValueError:
        return f"The number {num} is not in the sequence"
