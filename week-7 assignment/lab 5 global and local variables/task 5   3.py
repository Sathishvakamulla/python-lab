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

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit(amount)
        print("Amount deposited successfully")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == 3:
        print("Current balance:", balance)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")


'''output:1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter deposit amount: 500
Amount deposited successfully

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current balance: 1500.0

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 4
Thank you!'''
