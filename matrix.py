# def print_2D_array(array):
#    for i in range(0, len(array)):
#        for j in range(0, len(array[i])):
#            print("Row: " + str(i) + " Column: " + str(j) + " Element: " +
#                  str(two_dimensional_array[i][j]))

def find_zeros_in_matrix(matrix):
    list_of_zero_positions = [[]]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                list_of_zero_positions.append([i, j])
    return list_of_zero_positions

def validate_zero_position(zero_list, list_row, list_column):
    for i in range(0, len(zero_list)):
        for j in range(0, len(zero_list[i])):
            if zero_list[i][0] == list_row and zero_list[i][1] == list_column:
                return True
    return False

def set_matrix_zeros(matrix):
    zero_list = find_zeros_in_matrix(matrix)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0 and validate_zero_position(zero_list, i, j):
                # modify entire column, j = current column
                for k in range(0, len(matrix)):
                    matrix[k][j] = 0
                # modify entire row, i = current row
                for k in range(0, len(matrix[i])):
                    matrix[i][k] = 0
    return matrix

def print_2D_array_as_grid(array):
    for i in range(0, len(array)):
        print(array[i])

row = 10
column = 5

two_dimensional_array = [[0] * column] * row

jagged_array = [[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]]
test_matrix = [[1, 1, 1], [1 ,0, 1], [1, 1, 1]]

# print_2D_array(two_dimensional_array)
# print_2D_array(jagged_array)

second_test_matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print("Original")
print_2D_array_as_grid(test_matrix)
print("New")
set_matrix_zeros(test_matrix)
print_2D_array_as_grid(test_matrix)

print("\nOriginal")
print_2D_array_as_grid(second_test_matrix)
print("New")
set_matrix_zeros(second_test_matrix)
print_2D_array_as_grid(second_test_matrix)

# array to store position of zeros
# use array to pull out these numbers
# iterate through them, if they match [1, 2], e.g., then execute code
# matrix[row] == zero_list[row element] and matrix[column] == zero_list[column element]

# 1 [row 0][column 2] = 0
# 0 [row 1][column 2] = 0
# 1 [row 2][column 2] = 0
# 1 [row 3][column 2] = 0

# 1 0 1 -> 0 0 0
# [row 1][column 0, 1, 2] = 0