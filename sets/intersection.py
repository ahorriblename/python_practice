# get inputs
set_1 = input().split()
set_2 = input().split()

# convert string input into sets of ints
set_1 = set(map(int, set_1))
set_2 = set(map(int, set_2))

# get list of common elements and sort
list_of_both = list(set_1 & set_2)
list_of_both.sort()

# print common elements
for num in list_of_both:
    print(num, end = " ")