import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

@timer
def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = add(a, b)

print("Result:", result)


'''output:
Enter first number: 10
Enter second number: 20
Execution time: 1.19e-05 seconds
Result: 30'''
