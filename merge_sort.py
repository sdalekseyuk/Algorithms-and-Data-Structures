def merge(left_lst, right_lst):
    merged_lst = []
    i = j = 0
    while i < len(left_lst) or j < len(right_lst):
        if j == len(right_lst) or (i < len(left_lst) and left_lst[i] <= right_lst[j]):
            merged_lst.append(left_lst[i])
            i = i + 1
        else:
            merged_lst.append(right_lst[j])
            j = j + 1
    return merged_lst


def merge_sort(lst):
    list_length = len(lst)
    if list_length == 1:
        return lst
    left = lst[:list_length//2]
    right = lst[list_length//2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == '__main__':
    list_of_nums = [1, 8, 2, -1, 4, 7, -3, -2, 3, 6]
    list_of_nums = merge_sort(list_of_nums)
    print(list_of_nums)  # [-3, -2, -1, 1, 2, 3, 4, 6, 7, 8]
