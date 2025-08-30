"""
Understanding
Find the last non-zero digit of a factorial
Ex: Input: 4
    Output: 4

    Input: 5
    Output 2

Matching
Same as first_digit_factorial, but with the first digit instead of the last
"""

def calculate_factorial(num):
    factorial_result = 1

    for i in range(1, num + 1):
        factorial_result *= i
    
    return factorial_result

def get_last_digit(num):
    num_length =  len(str(num))
    last_digit = 0

    for i in range(0, num_length):
        last_digit = num % 10 ** (i + 1) // 10 ** i
        if last_digit == 0:
            continue
        else:
            break
    
    return last_digit

user_num = int(input())

factorial_result = calculate_factorial(user_num)

print(get_last_digit(factorial_result))