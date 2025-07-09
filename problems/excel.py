def test_ASCII():
    letter = "A"
    print(letter)
    print(ord(letter))

    # turn letter A into B -> (65 + 1) = B
    letter_B_num = ord(letter) + 1
    print(letter_B_num)
    # convert the number 66 into a letter -> B
    letter_B = chr(letter_B_num)
    print(letter_B)

def is_palindrome(string):
    reverse_string = string [::-1]
    if(reverse_string == string):
        print(string + " is a palindrome!")
        return True
    else:
        print(string + " is not a palindrome!")
        return False

is_palindrome("tacocat")

# step 1: create array
size = 26
letters = [0] * size
letter_numbers = [0] * size
# step 2: assign each letter a number using a loop
# letter 0 or A = 1, 1 = 2 etc
for i in range(0, 26):
    letters[i] = chr(i + 65)

for i in range(0, 26):
    letter_numbers[i] = i + 1

char = "A"
def iterate_letters(letter):
    for i in range(0 ,26):
        if letters[i] == letter:
            # print("Your char " + str(letters[i]) + " has a value of " + str(letter_numbers[i]) + "!")
            return letter_numbers[i]

# step 3: get user string
def get_title_number():
    print("Enter your column title: ")
    column_title = input() [::-1]

    # step 4: utilize array and if-else to get correct number
    result = 0
    current_letter_position = 0
    column_length = len(column_title)

    if (column_length <= 7 and column_length >= 1):
        for letter in column_title:
            current_number = iterate_letters(letter)
            if current_letter_position == 0:
                result += current_number
            else:
                result += (26 ** current_letter_position) * current_number
            current_letter_position += 1
    else:
        print("Invalid column title")
        return 0
    return result

print(get_title_number())