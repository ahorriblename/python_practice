"""
The text is given in a single line. For each word of the text count
the number of its occurrences before it.
"""

number_of_occurrences = {}
# get text
text = input().split()

for word in text:
    if word in number_of_occurrences:
        number_of_occurrences[word] += 1
        print(number_of_occurrences[word] - 1, end = " ")
    else:
        number_of_occurrences[word] = 1
        print(0, end = " ")