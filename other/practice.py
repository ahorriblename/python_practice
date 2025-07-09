'''

a = int(input())
print(a)
print(type(a))

b = [1,2,3]
print(type(b))

print(a + 2)

'''
import random

'''
a_string = "wow i went to the zoo the other day"

count = 1

for char in a_string:
    print(char + " " + str(count))
    count += 1

'''

#user_int = int(input())
#
#print("The next number for the number " + str(user_int) + " is " + str(user_int + 1))
#print("The previous number for the number " + str(user_int) + " is " + str(user_int - 1))
#print(6/2*(1+2))

#  (num % 1 + digit_power + 1 zero) // digit_power
#num = 5678
#
#first_digit = (num % 10000) // 1000
#second_digit = (num % 1000) // 100
#third_digit = (num % 100) // 10
#fourth_digit = (num % 10)
#
#print((num // 10 ** 3) % 10)

# i = digit_position starting from the last digit
# digit = (num % 10 ** digit_index) // 10 ** (digit_index - 1)

#print(first_digit)
#print(second_digit)
#print(third_digit)
#print(fourth_digit)
#
#print(5 % 4)
#print(1 / 9)

#num = int(input())
#first_digit = (num % 100) // 10
#second_digit = (num % 10)

#print(str(first_digit) + " " + str(second_digit))

#spending = float(input())
#earnings = float(input())

#spending_rate = (spending / earnings) * 100
#savings = earnings - spending
#savings_rate = (savings / earnings) * 100

#print("Your spending rate is " + str(spending_rate) + "% and your savings rate is "
#      + str(savings_rate) + "%.")


'''
# timestamp1 = 01:01:01
# timestamp2 = 02:02:02
hour1 = int(input())
minutes1 = int(input())
seconds1 = int(input())

hour2 = int(input())
minutes2 = int(input())
seconds2 = int(input())

# first convert everything to seconds
# 3600 seconds in an hour
hour_to_seconds1 = hour1 * 3600
minutes_to_seconds1 = minutes1 * 60

hour_to_seconds2 = hour2 * 3600
minutes_to_seconds2 = minutes2 * 60

result = (hour_to_seconds2 + minutes_to_seconds2 + seconds2) - (hour_to_seconds1
            + minutes_to_seconds1 + seconds1)
print(result)
'''

'''
num1 = float(input())
num2 = float(input())
num3 = float(input())

result = num1 + num2 + num3
result_string = str(result)
num_of_digits = len(result_string)
last_digit = int(result_string[num_of_digits - 1])

print(last_digit == 0)
'''

'''
num = float(input())

# get decimals
decimals = num % 1

# get first digit after decimal
first_digit = int(decimals * 10)
print(first_digit)
'''

'''
user_day = int(input())
print(((user_day + 3) % 7))
'''

'''
# get user input
num_of_minutes = int(input())
# calculate hours, 60 minutes in an hour
hours = num_of_minutes // 60
# calculate minutes, minutes leftover
minutes = num_of_minutes % 60
# print result
print(str(hours) + " " + str(minutes))
'''

'''
# get class sizes
class_size1 = int(input())
class_size2 = int(input())
class_size3 = int(input())

# calculate minimum amt of desks, if size % 2 != 0, add 1 to desk amt
# better to add remainder than to use if-else

if class_size1 % 2 != 0:
    desks1 = (class_size1 // 2) + 1
else:
    desks1 = class_size1 // 2

if class_size2 % 2 != 0:
    desks2 = (class_size2 // 2) + 1
else:
    desks2 = class_size2 // 2

if class_size3 % 2 != 0:
    desks3 = (class_size3 // 2) + 1
else:
    desks3 = class_size3 // 2

result = desks1 + desks2 + desks3
print(result)
'''

'''
# get user input
user_num = int(input())
# get second digit (tens) -> formula: (num % 100) // 10^1
tens_digit = (user_num % 100) // 10 ** 1
# print result
print(tens_digit)
'''

'''
# get user input (three digits)
user_digits = int(input())
# isolate all digits using remainder
# digit 1 (starting backwards) formula: (num % 10^1) // 10^0 (1)
digit1 = (user_digits % 10 ** 1) // (10 ** 0)
# digit 2 formula: (num % 10^2) // 10^1 (10)
digit2 = (user_digits % 10 ** 2) // (10 ** 1)
# digit 3 formula (num % 10^3) // 10^2 (100)
digit3 = (user_digits % 10 ** 3) // (10 ** 2)
# add all digits and print sum
sum_of_digits = digit1 + digit2 + digit3
print(sum_of_digits)
'''

'''
# input hour hand degrees
hour_degrees = int(input())
# minute hand moves 6 degrees per minute
# hour hand moves 0.5 degrees per minute
minute_degrees = 

# print how much the minute hand has moved since the CURRENT hour
'''

'''
# input km per day
km_per_day = int(input())
# input distance to cover
distance_to_cover = int(input())
# days = distance // km
days = distance_to_cover // km_per_day
# if remainder of calculation != 0, add an extra day
if distance_to_cover % km_per_day != 0:
    days += 1
# print days to cover distance
print(days)
'''

'''
# input year
year = int(input())
# 1st century = 1-100 -> 100 - 1 = 99
# 2nd = 101-200 -> 200 - 101 = 99

# get sum of digits of first two
digit1 = year % 10
digit2 = (year % 100) // 10
if (digit1 == 1 and digit2 == 0) or (digit1 == 0 and digit2 == 0):
    century = year % 99
else:
    century = (year // 100) + 1
print(century)
'''

'''
# input dollar cost
dollar_cost = int(input())
# input cent cost
cent_cost = int(input())
# input num of cupcakes to buy
num_of_cupcakes = int(input())
# calculate total cost
total_dollars = num_of_cupcakes * dollar_cost
total_cents = num_of_cupcakes * cent_cost
# convert dollars to cents
dollars_to_cents = total_dollars * 100
# total_cents now has the entire cost in cents
total_cents = total_cents + dollars_to_cents
# convert the cents to dollars
total_dollars = total_cents // 100
# get the remainder of the total cost for cents
total_cents = total_cents % 100
# output total cost in dollars and cents
print(str(total_dollars) + " " + str(total_cents))
'''

'''
# get 3 digit num
user_num = int(input())
# get each digit (reverse order)
third_digit = user_num % 10
second_digit = (user_num % 100) // 10
first_digit = (user_num % 1000) // 100
# check if the next digit is greater, if all true print YES, else print NO
if (first_digit < second_digit) and (second_digit < third_digit):
    print("YES")
else:
    print("NO")
'''

'''
# get user num (4 digits)
user_num = int(input())
# check if palindrome
# e.g 1234 NO, 2121 NO, 3443 YES
# 1234 -> 4321, 2121 -> 1212, 3443 -> 3443
# get digits right to left

# first half
# digit 1 (last digit) = num % 10 ex (1) or (3)
digit1 = user_num % 10
# digit 2 = num % 100 // 10 ex (2) or (4)
digit2 = user_num % 100 // 10
# second half
# digit 3 = num % 1000 // 100 ex (1) or (4)
digit3 = user_num % 1000 // 100
# digit 4 = num % 10000 // 1000 ex (2) or (3)
digit4 = user_num % 10000 // 1000

if (digit1 == digit4) and (digit2 == digit3):
    print("YES")
else:
    print("NO")
'''

'''
# get user package
package = input()
# get hours
hours = int(input())
# calculate costs for all three packages
hours_overtime_A = hours - 10
if hours_overtime_A <= 0:
    hours_overtime_A = 0
package_A_cost = (hours_overtime_A * 1.50) + 8.95

hours_overtime_B = hours - 20
if hours_overtime_B <= 0:
    hours_overtime_B = 0
package_B_cost = hours_overtime_B * 1.00 + 14.95

hours_overtime_C = hours - 40
if hours_overtime_C <= 0:
    hours_overtime_C = 0
package_C_cost = hours_overtime_C * .50 + 23.95

# compare package costs
if package == "A":
    package = package_A_cost
    differenceB = package - package_B_cost
    differenceC = package - package_C_cost

    string_package = str(format(package, ".2f"))
    savings = 0
    if package > package_B_cost or package > package_C_cost:
        if differenceB >= differenceC:
            savings = differenceB
            savings = format(savings, ".2f")
            print("Amount due: $" + string_package)
            print("You could save $" + str(savings) + " by switching to package B")
        else:
            savings = differenceC
            savings = format(savings, ".2f")
            print("Amount due: $" + string_package)
            print("You could save $" + str(savings) + " by switching to package C")
    else:
        print("Amount due: $" + string_package)
elif package == "B":
    package = package_B_cost
    differenceA = package - package_A_cost
    differenceC = package - package_C_cost

    string_package = str(format(package, ".2f"))
    savings = 0
    if package > package_A_cost or package > package_C_cost:
        if differenceA >= differenceC:
            savings = differenceA
            savings = format(savings, ".2f")
            print("Amount due: $" + string_package)
            print("You could save $" + str(savings) + " by switching to package A")
        else:
            savings = differenceC
            savings = format(savings, ".2f")
            print("Amount due: $" + string_package)
            print("You could save $" + str(savings) + " by switching to package C")
    else:
        print("Amount due: $" + string_package)
else:
    package = package_C_cost
    differenceA = package - package_A_cost
    differenceB = package - package_B_cost

    string_package = str(format(package, ".2f"))
    savings = 0
    if package > package_A_cost or package > package_B_cost:
        if differenceA >= differenceB:
            savings = differenceA
            savings = format(savings, ".2f")
            print("Amount due: $" + string_package)
            print("You could save $" + str(savings) + " by switching to package A")
        else:
            savings = differenceB
            savings = format(savings, ".2f")
            print("Amount due: $" + string_package)
            print("You could save $" + str(savings) + " by switching to package B")
    else:
        print("Amount due: $" + string_package)

# print out amount due for chosen package
# if cost is higher than other packages, print out highest difference package.
'''

'''
# get user num
user_num = int(input())
# print 1 if positive, num > 0
if user_num > 0:
    print(1)
# print -1 if negative, num < 0
elif user_num < 0:
    print(-1)
# print 0 if zero, num == 0
else:
    print(0)
'''

'''
# get user nums
num1 = int(input())
num2 = int(input())
# compare, num 1 < num 2, print num 1, else print num 2
if num1 < num2:
    print(num1)
else:
    print(num2)
# print the smaller num
'''

'''
# get user num
user_num = int(input())
# convert num to string, get length
num_length = len(str(user_num))
# if length == 3, print yes, else no
if num_length == 3:
    print("YES")
else:
    print("NO")
'''

'''
# get user nums (non-zero)
num1 = int(input())
num2 = int(input())
# if one is positive and the other is negative print YES, else NO
# create booleans
num1_is_positive = num1 > 0
num2_is_positive = num2 > 0

if (num1_is_positive and (not num2_is_positive)) or (
        (not num1_is_positive) and num2_is_positive):
    print("YES")
else:
    print("NO")
'''

'''
# get three nums
num1 = int(input())
num2 = int(input())
num3 = int(input())
# declare "greatest" variable
greatest = 0
# num1 > greatest, num1 == greatest, num2 > greatest, num2 == greatest, 
# num3 > greatest, num3 == greatest, use if instead of elif to run all conditions
if num1 > greatest:
    greatest = num1
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
# print greatest
print(greatest)
'''

'''
# get three nums
num1 = int(input())
num2 = int(input())
num3 = int(input())
# initialize "least" variable
least = num1
# num1 == least, num2 < least, num2 == least, num3 < least, num3 == least,
# use if instead of elif to run all conditions
if num2 < least:
    least = num2
if num3 < least:
    least = num3
# print least
print(least)
'''

'''
# get int 1-12 range (month)
month = int(input())

# Month # of days
# Jan: 31
# Feb: 28
# March: 31
# April: 30
# May: 31
# June: 30
# July: 31
# Aug: 31
# Sept: 30
# Oct: 31
# Nov: 30
# Dec: 31


# if num = respective month, print its # of days
if month == 1:
    print(31)
elif month == 2:
    print(28)
elif month == 3:
    print(31)
elif month == 4:
    print(30)
elif month == 5:
    print(31)
elif month == 6:
    print(30)
elif month == 7:
    print(31)
elif month == 8:
    print(31)
elif month == 9:
    print(30)
elif month == 10:
    print(31)
elif month == 11:
    print(30)
elif month == 12:
    print(31)
'''

'''
# get 3 nums
num1 = int(input())
num2 = int(input())
num3 = int(input())
# initialize count variable
equal_count = 0
# if num1 == num2, count++
if num1 == num2:
    equal_count += 1
# if num1 == num3, count++
if num1 == num3:
    equal_count += 1
# if num2 == num3, count++
if num2 == num3:
    equal_count += 1

if equal_count == 1:
    equal_count = 2

print(equal_count)
'''

'''
# get three nums
num1 = int(input())
num2 = int(input())
num3 = int(input())
# find outlier position
# position = num1, num2, num3
if num1 != num2 and num1 != num3:
    print(1)
if num2 != num1 and num2 != num3:
    print(2)
if num3 != num1 and num3 != num2:
    print(3)
'''

'''
# get year
year = int(input())
# check if leap year
# year % 4 == 0, year % 100 != 0 or year % 400 == 0
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")
'''

'''
# get num
num = int(input())
# get digit length using strings
num_length = len(str(num))
count = 0
# while count < length, num must be > 9
while count < num_length and num > 9 :
    # do formula
    # digit = (user_digits % 10 ** (count + 1)) // (10 ** count)
    current_digit = (num % 10 ** (count + 1)) // 10 ** count
    # increment count
    count += 1
    # print current num on same line
    print(current_digit, end="")
'''

'''
# define prices
apple_cost = 2.20
banana_cost = 1.50
orange_cost = 3.40
melon_cost = 4.10
# declare num of fruit variables
apple_num = 0
banana_num = 0
orange_num = 0
melon_num = 0
# while loop to prompt user, while input != "CHECKOUT", increment respective amount
while True:
    user_input = input()
    if user_input == "CHECKOUT":
        break

    if user_input == "Apple":
        apple_num += 1
    elif user_input == "Banana":
        banana_num += 1
    elif user_input == "Orange":
        orange_num += 1
    elif user_input == "Melon":
        melon_num += 1

# calculate total cost
total_cost = ((apple_num * apple_cost) + (banana_num * banana_cost)
              + (orange_num * orange_cost) + (melon_num * melon_cost))

# print cost of each item
if apple_num >= 1:
    print("Apples: $" + format(apple_cost * apple_num, ".2f"))
if banana_num >= 1:
    print("Bananas: $" + format(banana_cost * banana_num, ".2f"))
if orange_num >= 1:
    print("Oranges: $" + format(orange_cost * orange_num, ".2f"))
if melon_num >= 1:
    print("Melons: $" + format(melon_cost * melon_num, ".2f"))

# print total cost
print("Total: $" + format(total_cost, ".2f"))
'''

'''
# get num
num = int(input())
i = 1
while i ** 2 <= num:
    print(i ** 2, end=" ")
    i += 1
'''

'''
# get two ints
num1 = int(input())
num2 = int(input())
# print nums in range inclusively
for i in range(num1, num2 + 1):
    # print in one line
    print(i, end=" ")
'''

'''
# get user number, num <= 9
num = int(input())
# initialize ladderString
ladder_string = ""
for i in range(1, num + 1):
    # create new string and append the current digit, then print it.
    # ladderString = ladderString + current_digit
    ladder_string = ladder_string + str(i)
    print(ladder_string)
'''

'''
# get string
string = input()
# initialize count
count = 0
# for char in string
# ascii, letters = 65-122, whitespace == 32, 48-57 = numbers
# 65 <= char_decimal <= 122, (char_decimal == 32), (48 <= char_decimal <= 57)
for char in string:
    char_decimal = ord(char)
    is_punctuation = True
    if char_decimal == 32:
        is_punctuation = False
    elif 48 <= char_decimal <= 57:
        is_punctuation = False
    elif 65 <= char_decimal <= 122:
        is_punctuation = False

    if is_punctuation:
        count += 1

print(count)
'''

'''
search_num = int(input())

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
num7 = int(input())
num8 = int(input())

nums_list = [num1, num2, num3, num4, num5, num6, num7, num8]

for i in range(0, len(nums_list)):
    if nums_list[i] == search_num:
        print(i)
        break

    if i == 7:
        print("NOT FOUND")
'''

'''
# get num
num = int(input())
# get smallest divisor, not 1
# backwards loop
result = num

for i in range(num, 1, -1):
    if (num % i) == 0 and (num // i) != 1:
        if (num // i) < result:
            result = num // i

print(result)
'''

'''
# get num
num = int(input())
n = 0
result = 2 ** n
while result <= num:
    result = 2 ** n
    if result > num:
        n -= 1
        result = 2 ** n
        break
    n += 1

print(str(n) + " " + str(result))
'''

'''
num = 1
count = 0

while num != 0:
    num = int(input())
    if num != 0:
        count += 1
        
print(count)
'''

'''
sum = 0
num = 1

while num != 0:
    num = int(input())
    if num != 0:
        sum += num
print(sum)
'''

'''
sum = 0
num = 1
count = 0

while num != 0:
    num = int(input())
    if num != 0:
        sum += num
        count += 1

mean = sum / count
print(mean)
'''

'''
max = 0
num = 1

while num != 0:
    num = int(input())
    if num != 0:
        if max < num:
            max = num
print(max)
'''

'''
# LETS GO GAMBLING!
user_input = ""
earnings = 0
while user_input != "DONE":
    print("Bet: ", end="")
    user_input = input()

    if user_input == "DONE":
        break

    user_bet = int(user_input)

    num1 = random.randint(1, 7)
    num2 = random.randint(1, 7)
    num3 = random.randint(1, 7)


    if num1 == 7 and num2 == 7 and num3 == 7:
        user_bet *= 7
        earnings += user_bet
    elif num1 == num2 and num2 == num3:
        user_bet *= 3
        earnings += user_bet
    elif num1 == num2 or num2 == num3:
        user_bet *= 2
        earnings += user_bet
    else:
        user_bet -= user_bet * 2
        earnings += user_bet

    print(str(num1) + " " + str(num2) + " " + str(num3) + " " + str(user_bet))
print(earnings)
'''