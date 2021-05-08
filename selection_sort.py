def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[smallest], lst[i] = lst[i], lst[smallest]


if __name__ == '__main__':
    list_of_nums = [0, 7, -2, 11, 9, 2, 1, 5]
    selection_sort(list_of_nums)
    print(list_of_nums)  # [-2, 0, 1, 2, 5, 7, 9, 11]
