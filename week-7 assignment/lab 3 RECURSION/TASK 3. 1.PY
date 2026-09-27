def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


n = int(input("Enter a positive integer: "))

if n > 0:
    print("Sum of digits:", sum_of_digits(n))
else:
    print("Please enter a positive integer")


    '''OUTPUT:
Enter a positive integer: 12345
Sum of digits: 15'''
