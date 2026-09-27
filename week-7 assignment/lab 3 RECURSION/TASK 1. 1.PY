def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))

result = factorial(n)

print("Factorial of", n, "is", result)

'''OUTPUT:
Enter a number: 5
Factorial of 5 is 120'''
