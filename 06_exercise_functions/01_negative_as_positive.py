def sum_negative_and_positive_nums():
    negative_nums = []
    positive_nums = []
    for num in numbers:
        if num > 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)

    return sum(negative_nums), sum(positive_nums)


def bigger_sum(neg_and_pos_sum):
    negative_sum = abs(neg_and_pos_sum[0])
    positive_sum = neg_and_pos_sum[1]

    if negative_sum > positive_sum:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


numbers = [int(num) for num in input().split()]
negative_and_positive_sum = sum_negative_and_positive_nums()

print(*negative_and_positive_sum, sep='\n')
print(bigger_sum(negative_and_positive_sum))
