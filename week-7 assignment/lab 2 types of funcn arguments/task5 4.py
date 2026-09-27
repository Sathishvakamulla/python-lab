def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)

    print("Ordered Items:")
    for item in items:
        print("-", item)

    print("Discount:", discount, "%")


order_summary("Sathish", "Laptop", "Mouse", discount=10)


'''output:
Customer: Sathish
Ordered Items:
- Laptop
- Mouse
Discount: 10 %'''
