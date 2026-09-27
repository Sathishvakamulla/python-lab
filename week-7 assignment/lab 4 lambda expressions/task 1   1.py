
square = lambda x: x * x

even = lambda x: x % 2 == 0


larger = lambda x, y: x if x > y else y


n = int(input("Enter a number: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Square:", square(n))
print("Is even:", even(n))
print("Larger number:", larger(a, b))


'''output:
Enter a number: 8
Enter first number: 15
Enter second number: 22
Square: 64
Is even: True
Larger number: 22'''
