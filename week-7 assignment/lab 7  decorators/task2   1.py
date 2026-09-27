def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Return value:", result)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Result:", add(a, b))


'''output:
Enter first number: 10
Enter second number: 20
Function: add
Arguments: (10, 20) {}
Return value: 30
Result: 30'''
