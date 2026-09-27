def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("First 15 terms of Fibonacci series:")

for i in range(15):
    print(fibonacci(i), end=" ")

'''OUTPUT:
First 15 terms of Fibonacci series:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377'''
