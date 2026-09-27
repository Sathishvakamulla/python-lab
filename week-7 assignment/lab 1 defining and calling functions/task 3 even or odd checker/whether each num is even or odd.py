def is_even(n):
    """Check whether a number is even."""
    if n % 2 == 0:
        return True
    else:
        return False

for i in range(5):
    n = int(input("Enter a number: "))

    if is_even(n):
        print(n, "is Even")
    else:
        print(n, "is Odd


    '''output:
Enter a number: 45
45 is Odd
Enter a number: 7
7 is Odd
Enter a number: 24
24 is Even
Enter a number: 15
15 is Odd
Enter a number: 8
8 is Even'''
