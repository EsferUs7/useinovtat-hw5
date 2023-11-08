def largest_radial_sum(arr, d):
    n = len(arr)
    result = []
    for i in range(n // d):
        result.append(0)
        for j in range(i, n, n//d):
            result[i] += arr[j]
    return max(result)
