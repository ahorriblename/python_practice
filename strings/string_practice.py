"""
DOCUMENTING
"""

'''
# get string
string = input()
string_len = len(string)
# print the 3rd char \n
print(string[2])
# print second to last char \n
print(string[string_len - 2])
# print first 5 chars \n
print(string[0:5])
# print all chars except last two \n
print(string[0:string_len - 2])
# print chars with even index \n
for i in range(0, string_len):
    if i % 2 == 0:
        print(string[i], end = "")
# print chars with odd index \n
print()
for i in range(0, string_len):
    if i % 2 > 0:
        print(string[i], end = "")
# print reverse string \n
print()
reverse_string = string[::-1]
print(reverse_string)
# print every second char of reverse string \n e.g 1, 3, 5, 7
for i in range(0, string_len):
    if i % 2 == 0:
        print(reverse_string[i], end = "")
# print string length
print("\n" + str(string_len))
'''

'''
string = input()
first = string.find("f")
last = string.rfind("f")
if first == last:
    print(first)
elif first == -1:
    print(-1)
else:
    print(str(first) + " " + str(last))
'''

def get_second_occurrence(char):
    # get string
    string = input()
    # initialize p_count, result and string length variables
    count = 0
    result = 0
    string_len = len(string)
    for i in range(0, string_len):
      if string[i] == char:
          count += 1
      if count == 2 and result == 0:
          result = i
    # print -2 if there is no p in string
    if count == 0:
      result = -2
    # print -1 if there is only 1 p
    elif count == 1:
      result = -1

    return result

def remove_char_to_char(char):
    string = input()
    first = string.find(char)
    last = string.rfind(char)

    to_remove = string[first:last + 1]

    return string.replace(to_remove, "")

def replace_one_with_word():
    string = input()
    return string.replace("1", "one")

# delete indices divisible by 3, index % 3 == 0
# get string
string = input()
string_len = len(string)
replace_count = 0
# for loop
for i in range(0, string_len):
  if i % 3 == 0:
      # turn current index into empty string to "delete"
      to_replace = string[i - replace_count]
      string = string.replace(to_replace, "", 1)
      replace_count += 1
print(string)