from functools import reduce

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

result = reduce(
    lambda x, y: x + y,
    map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers))
)

print("Sum of squares of even numbers:", result)


'''output:
Enter number of elements: 5
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 6
Sum of squares of even numbers: 56'''
