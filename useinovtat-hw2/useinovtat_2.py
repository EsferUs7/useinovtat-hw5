def hanoi(tower):
    if tower == 1:
        return 1
    else:
        return 2*hanoi(tower-1) + 1
