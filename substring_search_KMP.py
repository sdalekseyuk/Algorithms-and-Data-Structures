def prefix(s):
    '''you can use Z-function instead of this'''
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


def kmp(s, subs):
    '''substring search with Knuth–Morris–Pratt'''
    len_subs = len(subs)
    subs += '#' + s
    arr = prefix(subs)
    result = []
    for i in range(0, len(arr)):
        if arr[i] == len_subs:
            result.append(i - len_subs - len_subs)
    return result


substring = 'aba'
string = 'abaCaba'
print(kmp(string, substring))  # -> [0, 4]