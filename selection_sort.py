def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[smallest], lst[i] = lst[i], lst[smallest]


# Verify it works
data = [-2, 45, 0, 11, 9]
selection_sort(data)
print(data)  # [-2, 0, 9, 11, 45]
