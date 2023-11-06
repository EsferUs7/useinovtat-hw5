def find_nb(m):
    value = 0
    n = 1

    while m > value:
        value += n*n*n
        n += 1

    if value > m:
        n = 0

    return n-1
