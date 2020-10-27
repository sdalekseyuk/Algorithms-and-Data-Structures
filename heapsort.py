def max_heapify(lst, heapsize, i):
    """Restoring heap properties"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heapsize and lst[left] > lst[i]:
        largest = left
    if right < heapsize and lst[right] > lst[largest]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heapify(lst, heapsize, largest)


def heap_sort(lst):
    heap_size = len(lst)
    # Build a max_heap
    for i in range(heap_size//2 - 1, -1, -1):
        max_heapify(lst, heap_size, i)
    # Max heapify
    for i in range(heap_size - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        max_heapify(lst, i, 0)


# Verify it works
random_list_of_nums = [1, 8, 20, 10, 4, 7, 30, 2, 3, 6]
heap_sort(random_list_of_nums)
print(random_list_of_nums)  # [1, 2, 3, 4, 6, 7, 8, 10, 20, 30]
