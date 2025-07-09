def get_max_index(a_list):
    # find max
    max = a_list[0]
    # find index
    index = 0
    for i in range(len(a_list)):
        item = a_list[i]
        if item > max:
            max = item
            index = i

    return (max, index)


# a_list = [int(str_numbers) for str_numbers in input().split() ] # Input list creation via list comprehension
# print(*get_max_index(a_list))
"""
def odd_occurences_of_number(nums):
    seen = []
    count = 0
    for num in nums:
        if num not in seen:
            count += 1
            seen.append((num, count))
        elif num in seen:
            
"""

def same_sign_neighbors(a_list):
    current = a_list[0]
    next = a_list[0]
    for i in range(0, len(a_list) - 1):
        next = a_list[i + 1]
        if (current > 0 and next > 0) or (current < 0 and next < 0):
            return current, next
        current = next
    return 0

# a_list = [int(str_numbers) for str_numbers in input().split()] # Input list
# result = same_sign_neighbors(a_list)
#
# if isinstance(result, tuple):
#     print(*result)
# else:
#     print(result)

def print_even_indices(a_list):
    for i in range(len(a_list)):
        if i % 2 == 0:
            print(a_list[i], end = " ")


a_list = [int(str_numbers) for str_numbers in input().split()]
# [expression for item in sequence if]
# new_list = [a_list[i] for i in range(len(a_list)) if i % 2 == 0]
# print(*new_list)
# new_list = [num for num in a_list if num % 2 == 0]
# print(*new_list)
def greater_than_left(a_list):
    result = []
    for i in range(1, len(a_list)):
        previous = a_list[i - 1]
        item = a_list[i]
        if item > previous:
            result.append(item)
    return result

# print(*greater_than_left(a_list))
# new_list = [a_list[i] for i in range(1, len(a_list)) if a_list[i] > a_list[i - 1]]
# print(*new_list)

def get_unique_elements(a_list):
    unique = []

    # for item in a_list:
    #     if item not in unique:
    #         unique.append(item)
    #     elif item in unique:
    #         unique.remove(item)
    #         if item in unique:
    #             unique.remove(item)
    new_list = []

    return unique

    # [expression for item in sequence if]

print(get_unique_elements(a_list))
