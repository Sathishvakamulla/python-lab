a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b <= c or b + c <= a or a + c <= b:
    print("Not a valid triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


'''output:
Enter side 1: 45
Enter side 2: 45
Enter side 3: 45
Equilateral'''
