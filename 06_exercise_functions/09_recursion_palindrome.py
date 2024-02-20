def palindrome(word, idx):
    # you check the first char of the word and the last char of the word
    # first base case
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    # second base case
    # if this is not returned the function continues
    if word[idx] != word[-idx-1]:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)

print(palindrome("abcba", 0))