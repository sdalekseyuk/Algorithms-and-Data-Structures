def scarecrow_sort(lst, distance):
    len_lst = len(lst)
    # split the main list into <distance> sublists
    for i in range(distance):
        # sort sublist
        sorted_part = sorted(lst[i:len_lst:distance])
        # return sorted values to their positions in the main list
        k = 0
        for j in range(i, len_lst, distance):
            lst[j] = sorted_part[k]
            k += 1
    # check if sorted and scarecrow_sorted lists are the same
    check = sorted(lst) == lst
    return check


# Verify it works
random_list = [1, 5, 3, 4, 1]
print(scarecrow_sort(random_list, 3))
# True
