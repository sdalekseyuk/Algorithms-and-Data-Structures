def insertion_sort(lst):
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > item_to_insert:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = item_to_insert


# Verify it works
list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(list_of_nums)
print(list_of_nums)  # [1, 6, 9, 15, 28]
