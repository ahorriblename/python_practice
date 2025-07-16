synonyms = {}

# first get num of full key-value pairs
num = int(input())

# get num amount of keys + values
for i in range(num):
    key, value = input().split()
    synonyms[key] = value

# get user synonym
user_synonym = input()

# find synonym of last key
for key, value in synonyms.items():
    if value == user_synonym:
        print(key)
    elif key == user_synonym:
        print(value)