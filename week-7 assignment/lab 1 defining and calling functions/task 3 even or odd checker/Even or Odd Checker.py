def is_even(n):
    """Check whether a number is even."""
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))

result = is_even(n)

print("Is even:", result)


''' output:
Enter a number: 45
Is even: False'''
