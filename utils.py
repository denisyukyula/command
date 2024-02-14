def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
(pull yulla)

def power_of_five(n):
    if n == 0:
        return False
    while n % 5 == 0:
        n /= 5
    return n == 1
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
