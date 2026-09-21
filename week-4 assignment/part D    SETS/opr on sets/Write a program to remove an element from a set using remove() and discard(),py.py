numbers = {10, 20, 30, 40}

numbers.remove(20)
print("After remove():", numbers)

numbers.discard(50)
print("After discard():", numbers)

# remove() gives an error if the element does not exist,
# but discard() does not give an error.


'''output:
After remove(): {40, 10, 30}
After discard(): {40, 10, 30}
'''
