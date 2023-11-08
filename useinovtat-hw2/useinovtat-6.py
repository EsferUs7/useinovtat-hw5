def land_perimeter(array):
    x_count = 0
    for i in array:
        for j in i:
            if j == 'X':
                x_count += 1

    neighbors = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'X':
                if j != 0:
                    if array[i][j-1] == 'X':
                        neighbors += 1
                if j != (len(array[i]) - 1):
                    if array[i][j+1] == 'X':
                        neighbors += 1
                if i != 0:
                    if j <= (len(array[i-1]) - 1):
                        if array[i-1][j] == 'X':
                            neighbors += 1
                if i != (len(array) - 1):
                    if j <= (len(array[i+1]) - 1):
                        if array[i+1][j] == 'X':
                            neighbors += 1

    answer = x_count*4 - neighbors
    return f'Total land perimeter: {answer}'
