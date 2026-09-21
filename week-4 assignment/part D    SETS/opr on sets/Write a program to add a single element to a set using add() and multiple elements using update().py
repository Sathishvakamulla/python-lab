numbers = {10, 20, 30}

numbers.add(40)
print("After add():", numbers)

numbers.update([50, 60, 70])
print("After update():", numbers)


'''output:
After add(): {40, 10, 20, 30}
After update(): {70, 40, 10, 50, 20, 60, 30}

'''
