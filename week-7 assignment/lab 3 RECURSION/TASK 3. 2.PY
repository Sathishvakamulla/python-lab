def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)


n = int(input("Enter a positive integer: "))

if n > 0:
    print("Reversed number:", reverse_number(n))
else:
    print("Please enter a positive integer")


    '''OUTPUT:
Enter a positive integer: 12345
Reversed number: 54321'''
