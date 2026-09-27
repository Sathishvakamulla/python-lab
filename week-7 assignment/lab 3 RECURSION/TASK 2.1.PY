def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the term number: "))

if n < 0:
    print("Fibonacci term is not defined for negative numbers")
else:
    print("Fibonacci term:", fibonacci(n))


    '''OUTPUT:Enter the term number: 6
Fibonacci term: 8'''
