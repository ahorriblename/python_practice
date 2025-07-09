
"""
# Two Halves
# get string
user_string = input()
string_len = len(user_string)
# cut into 2 equal parts
if string_len % 2 == 1:
    half1 = user_string[0:(string_len // 2 + 1)]
    half2 = user_string[(string_len // 2 + 1):string_len]
else:
    half1 = user_string[0:string_len // 2]
    half2 = user_string[string_len // 2:string_len]

print(half2 + half1)

# if odd len, keep center char in first half
# abcde - 5, 5/2 = 2
# abc [0,3]
# de [3,5]

# abcd - 4/2 = 2
# ab [0,2]
# de [2,4]

# print with halves swapped
"""
'''
word1, word2 = input().split()
swapped_string = word2 + " " + word1
print(swapped_string)
'''

def reverse_char_to_char(char):
    string = input()
    first = string.find(char)
    last = string.rfind(char)

    to_replace = string[first:last + 1]
    to_reverse = to_replace[::-1]

    return string.replace(to_replace, to_reverse)

def remove_char(char):
    string = input()
    return string.replace(char, "")

user_string = input()

first = user_string.find("h")
last = user_string.rfind("h")

# replace all h with H
user_string = user_string.replace("h", "H")

# replace first H with h
# slice[begin:end:step]
user_string = user_string[0:first] + "h" + user_string[first + 1:]
# replace last H with h
user_string = user_string[0:last] + "h" + user_string[last + 1:]

print(user_string)