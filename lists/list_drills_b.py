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
get_scale()