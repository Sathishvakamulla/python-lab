a= 25
MAX_VALUE = 100
def display():
    print("Function called successfully!")
class Student:
    name = "rohit"
user_name = "sharma"
s = Student()

print("Variable a :",a)
print("Constant-style name (MAX_VALUE):", MAX_VALUE)
print("Class name (Student):", s.name)
print("Identifier with underscore (user_name):", user_name)
display()




import keyword

identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
]

for name in identifiers:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(name, "-> Valid Identifier")
    else:
        print(name, "-> Invalid Identifier")







marks = 80
Marks = 95

print("marks =", marks)
print("Marks =", Marks)

