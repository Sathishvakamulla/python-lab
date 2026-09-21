numbers = (10, 20, 30)

try:
    numbers[0] = 100
except TypeError:
    print("Tuples are immutable")

'''output:
Tuples are immutable
'''
