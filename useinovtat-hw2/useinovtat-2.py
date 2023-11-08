def find_even_index(arr):
    i = 0
    while i < len(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
        i += 1
    return -1
