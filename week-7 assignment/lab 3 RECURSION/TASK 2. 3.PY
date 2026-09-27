count = 0

def fibonacci(n):
    global count

    if n == 5:
        count += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(10)

print("Fibonacci(10):", result)
print("fibonacci(5) was computed", count, "times")


'''OUTPUT:
Fibonacci(10): 55
fibonacci(5) was computed 5 times'''
