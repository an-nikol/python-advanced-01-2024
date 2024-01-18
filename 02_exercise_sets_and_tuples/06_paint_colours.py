from collections import deque

original_string = deque(input().split())

main_colors = ["red", "yellow", "blue"]

secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

collected_colors = []

while original_string:
    first_str = original_string.popleft()
    # when there is only one substring left in original string
    last_str = original_string.pop() if original_string else ''

    # check combinations
    if first_str + last_str in main_colors or first_str + last_str in secondary_colors:
        collected_colors.append(first_str + last_str)
    elif last_str + first_str in main_colors or last_str + first_str in secondary_colors:
        collected_colors.append(last_str + first_str)
    else:  # no matches
        idx = len(original_string) // 2
        if len(first_str) > 1:
            original_string.insert(idx, first_str[:-1])
        if len(last_str) > 1:
            original_string.insert(idx, last_str[:-1])

# check for valid secondary colors from the ones we collected
for color in collected_colors:
    if color in secondary_colors:
        for element in secondary_colors[color]:
            if element not in collected_colors:
                collected_colors.remove(color)
                break
print(collected_colors)


#
# from collections import deque
# # 1
# words = deque(input().split())
# # 2 all colours we have. We use a set to check if we have a subset with result
# colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
#
# # 3 a dict with sets
# required_colors = {
#     # we have set to check if these colours are in the result
#     'orange': {'yellow', 'red'},
#     'purple': {'red', 'blue'},
#     'green': {'yellow', 'blue'}
#     }
# result = []
#
# while words:
#     first_word = words.popleft()
#     # edge case
#     second_word = words.pop() if words else ''
#
#     # tuple of two strings
#     for color in (first_word + second_word, second_word + first_word):
#         if color in colors:
#             result.append(color)
#             break
#     else:
#         for el in (first_word[:-1], second_word[:-1]):
#             if el:
#                 words.insert(len(words) // 2, el)
#
# for color in set(required_colors.keys()).intersection(result):
#     if not required_colors[color].issubset(result):
#         result.remove(color)
#
# print(result)


