def merge(left_lst, right_lst):
    """Function to merge two lists in sorted order"""
    merged_lst = []
    i = j = 0
    left_lst_len, right_lst_len = len(left_lst), len(right_lst)
    while i < left_lst_len or j < right_lst_len:
        if j == right_lst_len or (i < left_lst_len and left_lst[i] <= right_lst[j]):
            merged_lst.append(left_lst[i])
            i = i + 1
        else:
            merged_lst.append(right_lst[j])
            j = j + 1
            # to count number of inversions in the list
            # you need to add a counter:
            # the length of the left list - the current left index
            # counter = counter + (left_lst_len - i)
    return merged_lst


def merge_sort(lst):
    list_length = len(lst)
    # If the list is a single element, return it
    if list_length == 1:
        return lst
    # Divide the list into two parts
    left = lst[:list_length//2]
    right = lst[list_length//2:]
    # Sort and merge each half
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


random_list_of_nums = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)