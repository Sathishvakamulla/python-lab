from functools import reduce

numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

product = reduce(lambda x, y: x * y, numbers)

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print("Product:", product)
print("Maximum:", maximum)



'''output:Enter number of elements: 5
Enter number: 2
Enter number: 5
Enter number: 3
Enter number: 8
Enter number: 4
Product: 960
Maximum: 8'''
