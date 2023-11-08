# string sorting
def sort_str(string):
    if len(string) <= 1:
        return string
    a = string[0]
    smaller = ""
    equal = ""
    bigger = ""
    for i in string:
        if i < a:
            smaller += i
        elif i == a:
            equal += i
        elif i > a:
            bigger += i
    return sort_str(smaller) + equal + sort_str(bigger)


# main func
def group_anagrams(array):
    answer = []
    after_sort = []
    for i in array:
        element = sort_str(i)
        if element not in after_sort:
            after_sort.append(element)

    for i in after_sort:
        result = []
        for j in array:
            if i == sort_str(j):
                result.append(j)
        answer.append(result)

    return answer
