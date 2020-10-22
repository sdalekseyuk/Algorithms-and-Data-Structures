def counting_sort(lst, sorted_lst, num):

    array = [0 for _ in range(num)]

    for i in range(len(lst)):
        array[lst[i]] += 1

    for j in range(1, num):
        array[j] = array[j] + array[j - 1]

    for item in range(len(lst) - 1, -1, -1):
        sorted_lst[array[lst[item]] - 1] = lst[item]
        array[lst[item]] -= 1

    return sorted_lst


# Verify it works
random_list_of_nums = [10, 8, 2, 4, 6, 1, 3, 7, 5]
list_for_sorting = random_list_of_nums.copy()
max_number = 11  # max number in list + 1
result = counting_sort(random_list_of_nums, list_for_sorting, max_number)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 10]
