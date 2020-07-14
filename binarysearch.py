def binary_search(a, c):
    b = len(a)
    d = 0
    r = b - 1

    while d <= r:
        m = (d + r)//2
        if a[m] < c:
            d = m + 1
        elif a[m] > c:
            r = m - 1
        else:
            return m
        return 'not_found'
