import time
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper

@log_call
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
Calling add args=(10, 20) kwargs={}
Execution time: 0.000001 seconds
add returned 30
Result: 30'''
