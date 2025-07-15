"""
Given a non-empty array of integers nums, every element appears
twice except for one. Find that single one.

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element
which appears only once.
"""

def get_single_num_sorted(nums):
    nums.sort()
    for i in range(0, len(nums), 2):
        if i + 1 < len(nums):
            if nums[i] != nums[i + 1]:
                return nums[i]
        elif i >= len(nums) - 1:
            return nums[i]
    return -1

def get_single_num(nums):
    # o(n) space, o(n) + o(n) = o(n)
    # empty array to store numbers that have been seen for the first time
    seen = []
    # empty array to store the current number if it has already been seen
    not_single = []

    # o(n) + o(n) = o(n)
    for num in nums:
        # if the current number has been seen, this is at least the
        # second time it has been seen, thus add it to an array
        # that stores numbers that have been seen more than once.
        if num in seen:
            not_single.append(num)
        # if the current number has not been seen, add it to an array
        # of seen numbers.
        if num not in seen:
            seen.append(num)
    # now we compare all the numbers in the original array to the not_single
    # array, if the current number is NOT in this array, it has only been
    # seen once, thus it's the number we return
    for num in nums:
        if num not in not_single:
            return num

    return -1

def get_single_num_bitwise(nums):
    xor_out = 0
    for num in nums:
        xor_out = xor_out ^ num
    return xor_out
# 0 if not different
# 1 if different
# print(1 ^ 1)
sorted_list = [1, 1, 2, 2, 3, 4, 4]
rand_list = [9, 12, 4, 8, 12,4,2,11, 9,2,11, 7,7]
# print(get_single_num_sorted(sorted_list))
print(get_single_num(sorted_list))
print(get_single_num(rand_list))

print(get_single_num_bitwise(sorted_list))
print(get_single_num_bitwise(rand_list))