# 2 intervals, nested loop for 2d array
import ast


def merge_two_overlapping_intervals(a_list):
    # if not overlapping, return original list
    # if [1][0] is > [0][1], not overlapping
    # if [1][0] is <= [0][1], overlapping
    if a_list[1][0] > a_list[0][1]:
        return a_list
    # else, return merged lists, [0][0] to [1][1]
    else:
        if a_list[1][1] > a_list[0][1]:
            return [[a_list[0][0], a_list[1][1]]]
        else:
            return [[a_list[0][0], a_list[0][1]]]

def merge_three_overlapping_intervals(intervals):
    # if not overlapping, return original list
    # if [1][0] is > [0][1], not overlapping
    # if [1][0] is <= [0][1], overlapping

    # if [2][0] is > [2][1], not overlapping
    # if [2][0] is <= [2][1], overlapping
    result = []
    if intervals[1][0] > intervals[0][1] and intervals[2][0] > intervals[1][1]:
        return intervals
    else:
        # get first merged list if merge
        if intervals[1][0] <= intervals[0][1]:
            if intervals[1][1] > intervals[0][1]:
                result.append([intervals[0][0], intervals[1][1]])
            else:
                result.append([intervals[0][0], intervals[0][1]])
            # merge second and third list if merge
            if intervals[2][0] <= result[0][1]:
                if intervals[2][1] > intervals[1][1]:
                    result = [[result[0][0], intervals[2][1]]]
                else:
                    result = [[intervals[0][0], intervals[1][1]]]
            # else don't merge second list
            else:
                result.append(intervals[2])
        else:
            # first list not merged, append it
            result.append(intervals[0])
            # compare second list to third
            if intervals[2][0] <= intervals[1][1]:
                if intervals[1][1] > intervals[2][1]:
                    result.append([intervals[1][0], intervals[1][1]])
                else:
                    result.append([intervals[1][0], intervals[2][1]])
    return result
intervals = [[-5, 5], [4, 120], [20, 22]]
print(merge_three_overlapping_intervals(intervals))
