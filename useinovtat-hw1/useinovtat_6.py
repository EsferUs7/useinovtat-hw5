def sort_func(n):
    if len(n) <= 1:
        return n

    a = int(n[0])
    smaller = ''
    equal = ''
    bigger = ''

    for i in n:
        if int(i) < a:
            smaller += i
        elif int(i) == a:
            equal += i
        elif int(i) > a:
            bigger += i
    return sort_func(bigger) + equal + sort_func(smaller)

def descending_order(n):
    a = sort_func(str(n))
    return int(a)
