def simple_interest(principal, rate, time):
    """Calculate and return the simple interest."""
    si = (principal * rate * time) / 100
    return si

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

result = simple_interest(principal, rate, time)

print("Simple Interest =", result)



'''output:
Enter principal: 5000
Enter rate: 9
Enter time: 8
Simple Interest = 3600.0
'''
