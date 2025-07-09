'''
# Sum of 10 ints

result = 0

for i in range(0,10):
    current_num = int(input())
    result += current_num
print(result)
'''

'''
# Series - 2

# get two nums
num_A = int(input())
num_B = int(input())
# if num_A < B, print increasing order (1)
# else if num_A >= B, print decreasing order (-1)
# inclusive, +1 for increasing, -1 for decreasing

if num_A < num_B:
    arg_3 = 1
    num_B += 1
else:
    arg_3 = -1
    num_B -= 1

for i in range(num_A, num_B, arg_3):
    print(i, end= " ")
'''

'''
# Sum of N Numbers

# get num of iterations
num_of_iterations = int(input())
result = 0
# loop for n times, add inputs
for i in range(0, num_of_iterations):
    result += int(input())

print(result)
'''

'''
# Sum of Cubes

# get num of iterations
num_of_iterations = int(input())
# initialize result
result = 0

for i in range(1, num_of_iterations + 1):
    result += i ** 3

print(result)
'''

'''
# Factorial

# eg. 4! = 4 * 3 * 2 * 1
# get num
num = int(input())
result = 1
# backwards loop
for i in range(num, 1, -1):
    result *= i
print(result)
'''

'''
# Sum of Factorial

def calculate_factorial(num):
    factorial_result = 1
    # backwards loop
    for a in range(num, 1, -1):
        factorial_result *= a
    return factorial_result

user_num = int(input())
result = 0
for i in range(1, user_num + 1):
    result += calculate_factorial(i)

print(result)
'''

'''
# prime = divisible by itself and one
def list_of_primes(x):
    # Generates a list of primes numbers between 1 and x
    primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes


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


print(list_of_primes(100))
'''
