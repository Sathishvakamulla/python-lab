def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numbers = list(range(1, 51))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)


'''output:
Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]'''
