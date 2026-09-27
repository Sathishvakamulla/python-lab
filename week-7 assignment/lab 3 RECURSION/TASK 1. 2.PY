def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return None
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", n, "is", factorial(n))


'''OUTPUT:
Enter a number: 0
Factorial of 0 is 1'''
