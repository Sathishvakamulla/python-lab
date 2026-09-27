numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

cubes = list(map(lambda x: x ** 3, numbers))

print("Cubes:", cubes)


'''output:
Enter number of elements: 5
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 6
Cubes: [8, 27, 64, 125, 216]'''
