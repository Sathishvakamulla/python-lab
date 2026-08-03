percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance: "))

eligible = percentage > 75 and attendance > 90

print(eligible)