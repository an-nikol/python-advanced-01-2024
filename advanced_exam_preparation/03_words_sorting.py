def words_sorting(*args):
    some_dict = {}
    result = ""

    for word in args:
        if word not in some_dict:
            some_dict[word] = sum([ord(char) for char in word])

    if sum(some_dict.values()) % 2 == 0:
        some_dict = dict(sorted(some_dict.items(), key=lambda x: x[0]))
    else:
        some_dict = dict(sorted(some_dict.items(), key=lambda x: -x[1]))

    for word, count in some_dict.items():
        result += f"{word} - {count}\n"

    return result

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
