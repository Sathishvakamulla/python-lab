balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance = balance - amount
    else:
        print("Insufficient funds")

amount = float(input("Enter deposit amount: "))
deposit(amount)
print("Balance after deposit:", balance)

amount = float(input("Enter withdrawal amount: "))
withdraw(amount)
print("Balance after withdrawal:", balance)


'''output:
Initial balance: 1000
Enter deposit amount: 500
Balance after deposit: 1500.0
Enter withdrawal amount: 300
Balance after withdrawal: 1200.0'''
