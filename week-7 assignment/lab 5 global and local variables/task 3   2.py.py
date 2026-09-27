counter = 0

def change_counter():
    global counter
    counter = counter + 1

change_counter()

print("Counter:", counter)


'''output:
Counter: 1'''
