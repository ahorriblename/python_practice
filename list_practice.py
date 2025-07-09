"""
ex_list = [1,2,3, "code", "word"]

# [expression for item in sequence , if]

result = 0

for item in ex_list:
    if isinstance(item, int):
        result += item

print(sum([item for item in ex_list if isinstance(item, int)]))
"""

# Swap max and min

def swap_min_max(a_list):
    max = 0
    max_index = 0

    min = a_list[0]
    min_index = 0

    for i in range(len(a_list)):
        if a_list[i] > max:
            max = a_list[i]
            max_index = i
        if a_list[i] < min:
            min = a_list[i]
            min_index = i
    a_list[max_index] = min
    a_list[min_index] = max

# a_list = [int(str_numbers) for str_numbers in input().split() ] # Input list creation via list comprehension
# swap_min_max(a_list)
# print(*a_list)

def greater_than_neighbors(a_list):
    count = 0

    if len(a_list) == 1:
        return 0
    previous = a_list[0]
    next = a_list[1]

    for i in range(1, len(a_list) - 1):
        next = a_list[i + 1]
        current = a_list[i]

        if current > previous and current > next:
            count += 1
        print("Current: " + str(current))
        print("P: " + str(previous))
        print("N: " + str(next))
        previous = current
    return count


# cool = [1,2,3,4,5, 10, 2, 5, 1, 12, 1 , 1]
# print(greater_than_neighbors(cool))

def greater_than_neighbors_opt(a_list):

    if len(a_list) == 1:
        return 0

    # [expression for item in sequence , if]
    return sum([1
                for i in range(1, len(a_list) - 1)
                if a_list[i] > a_list[i - 1] and a_list[i] > a_list[i + 1]])

# print(greater_than_neighbors_opt(cool))

# return NEW list

def filter_distinct_elements(a_list):
#   create copy of list
#   remove dupes
#   track seen elements
    seen = []

    for i in range(len(a_list)):
        current_item = a_list[i]
        if current_item not in seen:
            seen.append(current_item)

    return seen
#   return NEW list without dupes
# dupe_list = [1, 1 ,1, 2, 3, 44, 4 ,4, 1 ,5]
# print(filter_distinct_elements(dupe_list))

def find_max_2D_list():
    rows, columns = input().split()

    rows = int(rows)
    columns = int(columns)

    new_list = []

    for i in range(rows):
        inputs = map(int, input().split())
        inputs = list(inputs)
        new_list.append(inputs)

    max = new_list[0][0]
    max_pos = [0, 0]
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            item = new_list[i][j]
            if item > max:
                max = item
                max_pos[0] = i
                max_pos[1] = j

    string_pos = str(max_pos[0]) + " " + str(max_pos[1])
    return string_pos

def check_queens_chessboard(x, y):
    seen_row = []
    seen_col = []

    # check if in same row
    for num in x:
        if num not in seen_row:
            seen_row.append(num)
        elif num in seen_row:
            return "YES"

    # check if in same column
    for num in y:
        if num not in seen_col:
            seen_col.append(num)
        elif num in seen_row:
            return "YES"

    # check if diagonal, differences of x and y are equal
    # (7,6), diagonal = (6,7), (5,8), (8,5), (5,4)
    # diff between start and end pos

    for count in range(len(x)):
        current_item_x = x[count]
        current_item_y = y[count]
        for i in range(len(x)):
            #print("X being compared: " + str(current_item_x))
            #print("Y being compared: " + str(current_item_x))
            #print("Iteration/Index: " + str(i))
            diff_x = abs(current_item_x - x[i])
            diff_y = abs(current_item_y - y[i])

            #print("Current X: " + str(x[i]))
            #print("Current Y: " + str(y[i]))

            #print("Current X Diff: " + str(diff_x))
            #print("Current Y Diff: " + str(diff_y))
            if count == i:
                continue
            if diff_x == diff_y:
                return "YES"



    """
     # set up board
    for i in range(8):
        x_coord = x[i]
        y_coord = y[i]
        board[x_coord][y_coord] = "Q"
    """
    """
    # check for same row
    for count in range(len(x)):
        current_item = x[count] # start at 1st item, 0
        for i in range(len(x)):
            print("Item being compared: " + str(current_item))
            print("Current item: " + str(x[i]))
            print("Iteration/Index: " + str(i))
            if count == i:
                continue
            if current_item == x[i]:
                return "YES"
    """


    """
    # not same row
    row_count = 0
    for i in range(len(board)):
        for item in range(len(board[i])):
            if item == "Q":
                row_count += 1
            if item == "Q" and row_count > 1:
                return "YES"
        row_count = 0
    """

    return "NO"

x = []
y = []
for inputs in range(8):
    a_list = [int(s) for s in input().split()] # Use list comprehension to get input data
    x.append(a_list[0])
    y.append(a_list[1])

print(check_queens_chessboard(x, y))