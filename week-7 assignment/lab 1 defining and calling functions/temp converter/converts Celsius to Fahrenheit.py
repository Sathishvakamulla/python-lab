def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

c = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(c)

print("Temperature in Fahrenheit =", fahrenheit)


'''output:
Enter temperature in Celsius: 26
Temperature in Fahrenheit = 78.8

'''
