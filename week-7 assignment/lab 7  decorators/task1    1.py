def greet(name):
    return "Hello " + name

f = greet
name = input("Enter your name: ")
print(f(name))

def execute(func, value):
    return func(value)

name = input("Enter your name again: ")
print(execute(greet, name))

def create_function():
    def message(name):
        return "Welcome " + name
    return message

new_function = create_function()

name = input("Enter your name: ")
print(new_function(name))


'''output:
Enter your name: Ravi
Hello Ravi
Enter your name again: Sita
Hello Sita
Enter your name: Amit
Welcome Amit'''
