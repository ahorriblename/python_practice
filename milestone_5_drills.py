# Input, Print, and Numbers Recap

def get_user_last_char_decimal():
    user_name = input()
    last_char = user_name[len(user_name) - 1]
    return ord(last_char)

def get_last_two_digits(num):
    last_digit = num % 10
    second_to_last_digit = num % 100 // 10
    return [second_to_last_digit, last_digit]

def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary_string = ""
    quotient = n
    while quotient != 0:
        remainder = str(quotient % 2)
        quotient //= 2
        binary_string += remainder
    return binary_string[::-1]

def binary_to_decimal(s):
    s = s[::-1]

    result = 0
    position = 0

    for digit in s:
        multiple = 2 ** position
        num = int(digit)
        result += num * multiple
        position += 1
    return result

def get_lsb(binary_string):
    string_length = len(binary_string)
    return int(binary_string[string_length - 1])

def get_nth_lsb(binary, n):
    if isinstance(binary, int):
        return (binary % 10 ** (n + 1)) // 10 ** n
    elif isinstance(binary, str):
        binary = binary[::-1]
        return binary[n]



'''
last_char_num = get_user_last_char_decimal()
digits_arr = get_last_two_digits(last_char_num)

lsb_last_digit = get_lsb(decimal_to_binary(digits_arr[0]))
lsb_second = get_lsb(decimal_to_binary(digits_arr[1]))

if lsb_last_digit == lsb_second:
    print("Lsb matches: " + str(lsb_last_digit) + " " + str(lsb_second))
else:
    print("Lsb does not match: " + str(lsb_last_digit) + " " + str(lsb_second))
'''

'''
# Compare Last Bit
num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

num1_binary = decimal_to_binary(num1)
num2_binary = decimal_to_binary(num2)

if get_lsb(num1_binary) == get_lsb(num2_binary):
    print("True")
else:
    print("False")
'''

'''
# Count Bits in nth Position
num1, num2, num3, num4, n = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)
n = int(n)

num1 = int(decimal_to_binary(num1))
num2 = int(decimal_to_binary(num2))
num3 = int(decimal_to_binary(num3))
num4 = int(decimal_to_binary(num4))

# formula = num % 10^n+1 // 10^n
# 0th = num % 10^1 // 10^0
# 1st = num % 10^2 // 10^1
num1_pos = get_nth_lsb(num1, n)
num2_pos = get_nth_lsb(num2, n)
num3_pos = get_nth_lsb(num3, n)
num4_pos = get_nth_lsb(num4, n)

result = num1_pos + num2_pos + num3_pos + num4_pos
print(result)
'''

num = int(input())

num = decimal_to_binary(num)[::-1]
print(num)
print(binary_to_decimal(num))

second_to_last = int(get_nth_lsb(num, 1))
last = int(get_nth_lsb(num, 0))

result = ((2 ** 0) * second_to_last) + ((2 ** 1) * last)
print(result)