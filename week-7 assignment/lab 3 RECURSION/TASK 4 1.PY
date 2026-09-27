def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

if exp < 0:
    print("Please enter a non-negative exponent")
else:
    print("Result:", power(base, exp))


    '''OUTPUT:
       Enter the base: 2
       Enter the exponent: 5
       Result: 32'''
