word_frequency = {}
# get number of lines
num_of_lines = int(input())
# get text
text = [0] * num_of_lines
for i in range(num_of_lines):
    # get line as list
    line = input().split()
    # iterate through each word in the current line
    for word in line:
        # if the word has already been added to the dictionary, increase count
        if word in word_frequency:
            word_frequency[word] += 1
        # otherwise, initialize the key and count
        else:
            word_frequency[word] = 1

# find the word with the highest frequency
greatest = 0
most_frequent_word = ""
greatest_key_letter_1 = ""
current_key_letter_1 = ""

for key, value in word_frequency.items():
    if value > greatest:
        greatest = value
        most_frequent_word = key
        greatest_key_letter_1 = key[0]
    elif value == greatest:
        current_key_letter_1 = key[0]
        # lower number = higher in alphabetical order
        # if previous key is greater(lower in order), change most frequent to current key
        if ord(greatest_key_letter_1.lower()) > ord(current_key_letter_1.lower()):
            # if true, change most frequent to current key and update 1st letter
            most_frequent_word = key
            greatest_key_letter_1 = key[0]

print(most_frequent_word)