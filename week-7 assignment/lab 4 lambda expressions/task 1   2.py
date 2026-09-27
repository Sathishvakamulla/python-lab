square = lambda x: x * x
even = lambda x: x % 2 == 0
larger = lambda x, y: x if x > y else y

print(square(5))
print(even(8))
print(larger(10, 15))


''' output:
25
True
15'''
