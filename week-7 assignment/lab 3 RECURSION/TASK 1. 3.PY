def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Recursive factorial:", factorial_recursive(n))


'''OUTPUT:
Enter a number: 7
Recursive factorial: 5040
'''
