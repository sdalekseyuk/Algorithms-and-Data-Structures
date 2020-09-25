def insertion_sort(lst):
    # We start sorting from the second element, because the first element is considered to be already sorted
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        # Keep a link to the index of the previous item
        j = i - 1
        # Move the elements of the sorted segment forward if they are larger than the element to insert
        while j >= 0 and lst[j] > item_to_insert:
            lst[j + 1] = lst[j]
            j -= 1
        # Insert element
        lst[j + 1] = item_to_insert
    return lst

