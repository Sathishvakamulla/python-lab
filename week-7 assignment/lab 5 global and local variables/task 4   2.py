def make_counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

counter = make_counter()

for i in range(5):
    print("Count:", counter())


'''output:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5'''
