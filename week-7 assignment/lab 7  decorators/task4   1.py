def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print("Hello", name)

name = input("Enter your name: ")

greet(name)


'''output:
Enter your name: Ravi
Hello Ravi
Hello Ravi
Hello Ravi'''
