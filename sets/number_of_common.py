"""
Given two lists of numbers, count how many numbers of the first
one occur in the second one.
"""

list_1 = set(input().split())
list_2 = set(input().split())

common = (list_1 & list_2)
print(len(common))