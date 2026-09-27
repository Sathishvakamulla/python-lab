def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
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
add returned 30
Result: 30'''
