def left_binary_search(array, key, left, right):
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            index = mid
            right = mid - 1
        elif array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return index


def right_binary_search(array, key, left, right):
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            index = mid
            left = mid + 1
        elif array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return index


def binary_search(array, key, left, right):
    left_index = -1
    right_index = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            left_index = left_binary_search(array, key, left, mid)
            right_index = right_binary_search(array, key, mid, right)
            return left_index, right_index
        elif array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return left_index, right_index


def search(lst, elem):
    """Function that searches for the first and last occurrence of an element in a list
    using a binary search"""
    first_occurrence = 0
    last_occurrence = len(lst) - 1
    first_occurrence, last_occurrence = binary_search(lst, elem, first_occurrence, last_occurrence)
    return first_occurrence, last_occurrence


random_list = [1, 1, 2, 2, 2]

num = 1
first, last = search(random_list, num)
print('{} {}'.format(first, last))  # -> 0 1

num = 2
first, last = search(random_list, num)
print('{} {}'.format(first, last))  # -> 2 4

num = 3
first, last = search(random_list, num)
print('{} {}'.format(first, last))  # -> -1 -1
