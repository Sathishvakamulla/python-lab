dict1 = {1: "Ravi", 2: "Sita"}
dict2 = {3: "Arjun", 4: "Priya"}

dict3 = dict1.copy()
dict3.update(dict2)
print("Using update():", dict3)

dict4 = dict1 | dict2
print("Using | operator:", dict4)


'''output:
Using update(): {1: 'Ravi', 2: 'Sita', 3: 'Arjun', 4: 'Priya'}
Using | operator: {1: 'Ravi', 2: 'Sita', 3: 'Arjun', 4: 'Priya'}

'''
