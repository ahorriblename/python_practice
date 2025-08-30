"""
Understanding
    Input: non-negative number (n > 0)
    Output: first digit of factorial number

    Ex: Input = 4
        Output = 2
        1 * 2 * 3 * 4 = 24

        Input = 3
        Output = 6
        1 * 2 * 3 = 6

    We must find the factorial of a number, and then return the first digit.

Matching
    I have done a problem in the past to calculate factorials. I know that I will need to use
    a for loop starting from 1. I also know that I can use modulo to get a specific digit
    from number, using the following formula: num % 10^n+1 // 10^n
"""

# Plan
# get user input
# initalize result variable

# find factorial
# Use for loop
# for i in range(1, num + 1):
#   factorial_result *= i

# turn result into string and get length
# initalize last_digit
# for loop to run for length
#   last_digit = num % 10^i+1 // 10^i
# print last_digit

def calculate_factorial(num):
    factorial_result = 1

    for i in range(1, num + 1):
        factorial_result *= i
    
    return factorial_result

def get_first_digit(num):
    num_length = len(str(num))
    first_digit = 0

    for i in range(0, num_length):
        first_digit = num % 10 ** (i + 1) // 10 ** i
    return first_digit

user_num = int(input())

factorial_result = calculate_factorial(user_num)
print(get_first_digit(factorial_result))
