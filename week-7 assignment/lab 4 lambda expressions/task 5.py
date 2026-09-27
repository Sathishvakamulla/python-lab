items = {}

n = int(input("Enter number of items: "))

for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    items[name] = price

sorted_items = sorted(items.items(), key=lambda x: x[1])

print("Items from cheapest to most expensive:")

for item in sorted_items:
    print(item[0], ":", item[1])


'''output:
Enter number of items: 4
Enter item name: Pen
Enter price: 20
Enter item name: Book
Enter price: 80
Enter item name: Bag
Enter price: 500
Enter item name: Pencil
Enter price: 10

Items from cheapest to most expensive:
Pencil : 10.0
Pen : 20.0
Book : 80.0
Bag : 500.0'''
