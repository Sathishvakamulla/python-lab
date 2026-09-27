def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Ordered Items:")

    for item in items:
        print("-", item)


order_summary("Sathish", "Laptop", "Mouse", "Keyboard")


'''output:
Customer: Sathish
Ordered Items:
- Laptop
- Mouse
- Keyboard'''
