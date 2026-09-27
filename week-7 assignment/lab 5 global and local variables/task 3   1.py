counter = 0

def change_counter():
    counter = counter + 1

change_counter()

'''output:
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value'''
