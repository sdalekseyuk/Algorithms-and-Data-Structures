def foo(string):
    """the number of ways to delete from the message all letters except three
    so that the remaining word is equally read from left to right and from right to left"""
    string = string.replace(" ", '')
    counter = 0
    d = {}
    for i in range(len(string)):
        if string[i] in d:
            curr_diff = i - d[string[i]][1] - 1
            x = curr_diff + (curr_diff + 1) * d[string[i]][0] + d[string[i]][2]
            counter += x
            d[string[i]][0] += 1
            d[string[i]][1] = i
            d[string[i]][2] = x
        else:
            d[string[i]] = [0, i, 0]
    return counter


some_string = 'treasure'
print(foo(some_string))  # -> 8
some_string = 'you will never find the treasure'
print(foo(some_string))  # -> 146
