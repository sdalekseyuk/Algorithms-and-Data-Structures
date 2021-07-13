def insertion_sort(lst):
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > item_to_insert:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = item_to_insert


if __name__ == '__main__':
    list_of_nums = [9, 1, -3, 15, 28, 6, -5, 0, 7]
    insertion_sort(list_of_nums)
    print(list_of_nums)  # [-5, -3, 0, 1, 6, 7, 9, 15, 28]
