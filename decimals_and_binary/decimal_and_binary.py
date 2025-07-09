def decimal_to_binary(n):
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

print(decimal_to_binary(int(input())))