numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

result = list(filter(lambda x: x % 3 == 0, numbers))

print("Numbers divisible by 3:", result)


''' output:
Enter number of elements: 6
Enter number: 3
Enter number: 7
Enter number: 9
Enter number: 12
Enter number: 14
Enter number: 18
Numbers divisible by 3: [3, 9, 12, 18]'''
s
