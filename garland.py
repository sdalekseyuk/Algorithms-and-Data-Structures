def garland(n, height):
    """Function that calculates the minimum height of the end of the garland"""
    lst = [0.0] * n
    lst[0] = height
    left = 0
    right = lst[0]
    while right - left > 0.00000000001:
        lst[1] = (left + right) / 2
        check = True
        for i in range(2, n):
            lst[i] = 2 * lst[i - 1] - lst[i - 2] + 2
            if lst[i] < 0:
                check = False
                break
        if check:
            right = lst[1]
        else:
            left = lst[1]
    return lst[n - 1]


# Verify it works
N = 8
A = 15.0
B = garland(N, A)
print(B)  # 9.75

N = 692
A = 532.81
B = garland(N, A)
print(B)  # 446113.34434782993
