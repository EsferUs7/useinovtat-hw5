def is_prime(number):
    d = 2
    value = True
    if number <= 1:
        value = False
    else:
        while d*d <= number:
            if number % d == 0:
                value = False
                return value
            d += 1
    return value
