numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum([x ** 2 for x in numbers if x % 2 == 0])

print("Sum of squares of even numbers:", total)



'''output:
Enter number of elements: 10
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 6
Enter number: 7
Enter number: 8
Enter number: 9
Enter number: 10
Sum of squares of even numbers: 220'''
