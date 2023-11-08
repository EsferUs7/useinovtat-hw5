def solution(n):
    suma = 0
    if n < 4:
        return 0
    else:
        for i in range(3, n):
            if i % 3 == 0 or i % 5 == 0:
                suma += i
        return suma
