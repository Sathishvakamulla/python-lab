def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

result = simple_interest(principal, rate, time)

print("Simple Interest =", result)


'''output:
Enter principal: 5000
Enter rate: 8
Enter time: 6
Simple Interest = 2400.0
'''
