from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    limit = sqrt(number)
    i = 2
    while i <= limit:
        if number % i == 0:
            return False
        i += 1
    return True


print(is_prime(3))
