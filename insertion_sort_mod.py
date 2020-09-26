def insertion_sort(lst):
    """Modified insertion sort"""
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0 and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1
    return lst