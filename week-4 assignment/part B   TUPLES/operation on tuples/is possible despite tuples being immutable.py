data = ("Apple", [10, 20, 30], "Mango")

data[1].append(40)

# Tuple is immutable, but the nested list inside it is mutable.

print(data)


'''output:

('Apple', [10, 20, 30, 40], 'Mango')

'''
