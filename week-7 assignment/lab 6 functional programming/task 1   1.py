def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

temperatures = []

n = int(input("Enter number of temperatures: "))

for i in range(n):
    temp = float(input("Enter temperature in Celsius: "))
    temperatures.append(temp)

fahrenheit = list(map(celsius_to_fahrenheit, temperatures))

print("Temperatures in Fahrenheit:", fahrenheit)

'''output:
Enter number of temperatures: 4
Enter temperature in Celsius: 0
Enter temperature in Celsius: 25
Enter temperature in Celsius: 30
Enter temperature in Celsius: 100
Temperatures in Fahrenheit: [32.0, 77.0, 86.0, 212.0]'''
