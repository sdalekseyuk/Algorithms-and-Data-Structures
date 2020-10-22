def binary_search(lst, key):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == key:
            return mid
        if lst[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# Verify it works
random_list_of_nums = [1, 3, 5, 8, 10]
item = 8
result = binary_search(random_list_of_nums, item)
print(result)  # => 3
