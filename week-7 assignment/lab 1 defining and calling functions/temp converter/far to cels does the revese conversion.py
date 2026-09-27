def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


c = float(input("Enter temperature in Celsius: "))
f = float(input("Enter temperature in Fahrenheit: "))

print("Fahrenheit =", celsius_to_fahrenheit(c))
print("Celsius =", fahrenheit_to_celsius(f))


'''output:
Enter temperature in Celsius: 26
Enter temperature in Fahrenheit: 78
Fahrenheit = 78.8
Celsius = 25.555555555555557

'''
