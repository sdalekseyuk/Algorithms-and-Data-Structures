import math


def find_max_cross_subarray(lst, low, mid, high):
    left_sum = -math.inf
    sum = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sum += lst[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -math.inf
    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum += lst[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return left_sum + right_sum, max_left, max_right


def find_max_subarray(lst, low, high):
    if high == low:
        return lst[low], low, high
    else:
        mid = (low + high) // 2
        left_sum, left_low, left_high = find_max_subarray(lst, low, mid)
        right_sum, right_low, right_high = find_max_subarray(lst, mid + 1, high)
        cross_sum, cross_low, cross_high = find_max_cross_subarray(lst, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum, left_low, left_high
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum, right_low, right_high
        else:
            return cross_sum, cross_low, cross_high


if __name__ == '__main__':
    list_of_nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    max_sum, start, end = find_max_subarray(list_of_nums, 0, len(list_of_nums) - 1)
    print(max_sum, start, end)  # 43 7 10

