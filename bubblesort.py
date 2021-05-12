def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == '__main__':
    list_of_nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(list_of_nums)
    print(list_of_nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
