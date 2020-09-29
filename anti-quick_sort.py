def anti_quick_sort(input_n):
    n = input_n
    lst = [i + 1 for i in range(n)]
    for i in range(2, n):
        lst[i], lst[i // 2] = lst[i // 2], lst[i]
    return lst


# Verify it works
print(anti_quick_sort(5))
# [1, 4, 5, 3, 2]
