from string import punctuation
import os

# create the path for the text that will be read
path = os.path.join("text.txt")

# open the text you will be reading
with open(path, "r") as text_file:
    # save all the lines of the text that we will be reading in a list with strings/n
    text = text_file.readlines()

# create our new doc "for writing"
output_file = open("output_2.txt", "w")

# start iterating through our FIRST doc
for row in range(len(text)):
    letters, marks = 0, 0
    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1
    # write the new content
    output_file.write(f"Line {row + 1}: {''.join(text[row])[:-1]} ({letters}) ({marks})\n")



output_file.close()
