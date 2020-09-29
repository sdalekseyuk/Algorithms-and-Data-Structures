def quicksort(lst, low, high):
    if low >= high:
        return

    i, j = low, high
    pivot = lst[(high + low) // 2]

    while i <= j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i, j = i + 1, j - 1
    quicksort(lst, low, j)
    quicksort(lst, i, high)


# Verify it works
random_list_of_nums = [99, 4, 5, 5, 44, 10, 20, -1]
quicksort(random_list_of_nums, 0, len(random_list_of_nums) - 1)
print(random_list_of_nums)
