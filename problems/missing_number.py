"""
Given a list, nums, containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the list.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""

# iterate through the arr
# range(max num)
# if all numbers in range are present, missing = n + 1
# if current_item not in range(num), item == missing
#   [3,0,1]
#
# return missing

def get_missing_num_sorted(sorted_list):
    range_list = range(len(sorted_list))
    for num in range_list:
        if num not in sorted_list:
            return num
        if num == len(sorted_list) - 1:
            return num + 1
    return -1

def get_missing_num_sort(a_list):
    a_list.sort()
    range_list = range(len(a_list))
    for num in range_list:
        if num not in a_list:
            return num
        if num == len(a_list) - 1:
            return num + 1
    return -1

def get_missing_num_unsorted(a_list):
    # o(n) space complexity
    range_list = range(len(a_list))

    # loop has o(n) time complexity
    for num in range_list:
        # in has o(n) time complexity
        if num not in a_list:
            return num
        if num == len(a_list) - 1:
            return num + 1

    return -1

def get_missing_num_unsorted_const(a_list):
    # o(1) space complexity
    range_list = range(10 ** 4)

    # loop has o(n) time complexity
    for num in range_list:
        # in has o(n) time complexity
        if num not in a_list:
            return num
        if num == len(a_list) - 1:
            return num + 1

    return -1

def get_missing_num_unsorted_sum(integers):
    # o(1) space complexity
    list_len = len(integers)
    list_sum = 0
    main_sum = (list_len * (list_len + 1)) // 2
    # loop has o(n) time complexity
    for num in integers:
        list_sum += num
    return main_sum - list_sum


sorted_list = [0, 1, 2, 3, 4, 6, 7]
rand_list = [7, 2, 3, 6, 4, 1, 5, 12, 0, 13, 9, 10, 11]
big_list = [i for i in range(2000)]

print(get_missing_num_sorted(sorted_list))
print(get_missing_num_sort(rand_list))
print(get_missing_num_unsorted(big_list))
print(get_missing_num_unsorted_const(big_list))

print(get_missing_num_unsorted_sum(rand_list))
print(get_missing_num_unsorted_sum(sorted_list))