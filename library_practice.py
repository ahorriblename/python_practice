import string
import random
import math

"""
user_string = input()
result = False

for char in user_string:
    if char in string.hexdigits:
        result = True
    elif not char in string.hexdigits:
        result = False
        break
print(result)
"""
def random_letter(ex_str):
    rand_index = random.randint(0, len(ex_str) - 1)
    return ex_str[rand_index]

def perimeter(ax, ay, bx, by, cx, cy):
    a = [ax, ay]
    b = [bx, by]
    c = [cx, cy]

    len_a = math.dist(a,b)
    len_b = math.dist(a,c)
    len_c = math.dist(c,b)
    return len_a + len_b + len_c

print(perimeter(0, 0, 3, 0, 0, 4))