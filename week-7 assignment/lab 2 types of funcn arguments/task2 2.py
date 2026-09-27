def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    discount_amount = price * discount / 100
    final_price = price + tax - discount_amount
    return final_price

price = float(input("Enter price: "))


print("Only price:", calculate_price(price))


tax_rate = float(input("Enter custom tax rate: "))
print("Custom tax rate:", calculate_price(price, tax_rate))

tax_rate = float(input("Enter tax rate: "))
discount = float(input("Enter discount: "))
print("All arguments:", calculate_price(price, tax_rate, discount))


'''output:
Enter price: 1000
Only price: 1180.0
Enter custom tax rate: 10
Custom tax rate: 1100.0
Enter tax rate: 10
Enter discount: 5
All arguments: 1050.0'''
