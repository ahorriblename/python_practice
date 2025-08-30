"""
- Understanding

Description: Given an integer n, return the number of prime numbers that are 
strictly less than n.

We must return an integer, the number of prime numbers, NOT the prime numbers themselves, 
that is our output.

The input is an integer, and it must also be greater than 0.

Examples: Input: 10, Output: 4 (2, 3, 5, 7)
Input: 15, Output: 6 (2, 3, 5 ,7, 11 , 13)

- Match
When we were working with for loops, we had to generate a list of prime numbers. I can use
the logic from that problem here, and return the number of prime numbers instead of the
numbers themselves. We will need both conditionals and for loops. We will need to loop through
a range up to the number provided, excluding the number itself. We will need multiple loops,
but no nested loops.
"""

# - Plan
# Get user input, int, greater than 0
# Create prime_count

# Determine if current number is prime
# Prime numbers only have 2 factors, find number of factors for current num
# def is_prime(number):
#   Create factor_count variable

#   Use for loop to check if the numbers in the range up to the given number are divisible.
#   for i in range(1, num + 1), start at 1 to exclude 0, num + 1 to include the number itself
#       if num % i == 0
#           increment factor count

# Check if factor_count is > than 2
# if factor_count > 2:
#   return False
# else
#   return True

# for i in range(user_number):
#   if is_prime(i):
#       prime_count += 1
# return prime_count

def is_prime(num):
    factor_count = 0
    for i in range(1, num + 1):
        if num == 1:
            return False

        if num % i == 0:
            factor_count += 1

    if factor_count > 2:
        return False
    else:
        return True

def num_of_prime(num):
    prime_count = 0

    for i in range(1, num):
        if is_prime(i):
            prime_count += 1
    
    return prime_count

user_num = int(input())

print(num_of_prime(user_num))