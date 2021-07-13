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
    # Sorting with max_heapify
    for i in range(heap_size - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        max_heapify(lst, i, 0)


if __name__ == '__main__':
    list_of_nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heap_sort(list_of_nums)
    print(list_of_nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
