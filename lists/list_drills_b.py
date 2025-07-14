def get_scale():
    # get rows and columns
    rows, columns = input().split()
    rows = int(rows)
    columns = int(columns)
    # input elements
    new_list = []

    for i in range(rows):
        inputs = map(int, input().split())
        inputs = list(inputs)
        new_list.append(inputs)
    # multiply all elements by this num
    scale = int(input())

    for i in range(len(new_list)):
        if i > 0:
            print()
        for j in range(len(new_list[i])):
           new_list[i][j] *= scale
           print(new_list[i][j], end = " ")

    return new_list
# get_scale()

def create_diagonal_list(num):
    new_list = [[0 for i in range(num)] for j in range(num)]
    lower_diag = 0
    upper_diag = 0
    for i in range(num):
        for j in range(num):
            # print(str(i) + " " + str(j) + " = " + str(new_list[i][j]))
            if i == j:
                new_list[i][j] = 0
                count = 1
                # above = [i + 1][j], below = [i - 1][j], next[i][j + 1], prev[i][j - 1]
                if i + 1 < num:
                    new_list[i + 1][j] = 1
                if i - 1 >= 0:
                    new_list[i - 1][j] = 1
                if j + 1 < num:
                    new_list[i][j + 1] = 1
                if j - 1 >= 0:
                    new_list[i][j - 1] = 1
                to_add = 2
                # adj diagonal, [2][2] = [3][1], [4][0], [1][3], [0][4]
                # [i + 1][j - 1], [i + 2][j - 2], [i - 1][j + 1], [i - 2][j + 2]
                # count = 1, [i + count][j - count], [i - count][j + count]
                # count += 1
                while i + count < num and j - count >= 0 and j + count < num and j - count >= 0:
                    new_list[i + count][j - count] = to_add
                    new_list[i - count][j + count] = to_add
                    to_add += 2
                    count += 1
            if i + 1 < num and j - 1 >= 0:
                lower_diag = new_list[i + 1][j - 1]
            if j + 1 < num and j - 1 >= 0:
                upper_diag = new_list[i - 1][j + 1]
            if new_list[i][j] == 1 and lower_diag == 1:
                count = 1
                to_add = 3
                while i + count < num and j - count >= 0 and j + count < num and j - count >= 0:
                    new_list[i - count][j + count] = to_add
                    to_add += 2
                    count += 1
            if new_list[i][j] == 1 and upper_diag == 1:
                count = 1
                to_add = 3
                while i + count < num and j - count >= 0 and j + count < num and j - count >= 0:
                    new_list[i + count][j - count] = to_add
                    to_add += 2
                    count += 1

    return new_list
a_list = create_diagonal_list(7)
for row in a_list:
    print(*row)