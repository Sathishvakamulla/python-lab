def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))


''' output:
Enter principal: 500
Enter rate: 3
Enter time: 2
Simple Interest = 30.0
'''
n
