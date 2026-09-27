def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Items:", items)
    print("Discount:", discount, "%")
    print("Extra Details:")

    for key, value in extra.items():
        print(key.capitalize(), ":", value)


order_summary(
    "Sathish",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=10,
    city="Hyderabad",
    payment="UPI"
)


'''output:
Customer: Sathish
Items: ('Laptop', 'Mouse', 'Keyboard')
Discount: 10 %
Extra Details:
City : Hyderabad
Payment : UPI'''
