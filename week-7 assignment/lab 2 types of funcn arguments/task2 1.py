def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    discount_amount = price * discount / 100
    final_price = price + tax - discount_amount
    return final_price

price = float(input("Enter price: "))

print("Final price:", calculate_price(price))


'''output:
Enter price: 100
Final price: 118.0
'''
