n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count = count + 1


'''output-
Enter number of terms: 10
0 1 1 2 3 5 8 13 21 34 
'''
