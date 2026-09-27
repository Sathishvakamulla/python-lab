def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)

    print("Ordered Items:")
    for item in items:
        print("-", item)

    print("Discount:", discount, "%")

    print("Extra Information:")
    for key, value in extra.items():
        print(key, ":", value)


order_summary(
    "Sathish",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap="Yes"
)


'''output:
Customer: Sathish
Ordered Items:
- Laptop
- Mouse
Discount: 10 %
Extra Information:
delivery_address : Hyderabad
gift_wrap : Yes'''
