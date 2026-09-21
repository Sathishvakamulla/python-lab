items = {
    "Pen": 10,
    "Book": 50,
    "Bag": 100,
    "Pencil": 5
}

highest = max(items, key=items.get)
lowest = min(items, key=items.get)

print("Highest price:", highest, items[highest])
print("Lowest price:", lowest, items[lowest])


''' output:
Highest price: Bag 100
Lowest price: Pencil 5
'''
