numbers = [10, 20, 30, 20, 40]

numbers.append(50)
print("append:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.extend([60, 70])
print("extend:", numbers)

numbers.remove(20)
print("remove:", numbers)

numbers.pop()
print("pop:", numbers)

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

print("count of 20:", numbers.count(20))
print("index of 40:", numbers.index(40))


'''output:
append: [10, 20, 30, 20, 40, 50]
insert: [10, 15, 20, 30, 20, 40, 50]
extend: [10, 15, 20, 30, 20, 40, 50, 60, 70]
remove: [10, 15, 30, 20, 40, 50, 60, 70]
pop: [10, 15, 30, 20, 40, 50, 60]
sort: [10, 15, 20, 30, 40, 50, 60]
reverse: [60, 50, 40, 30, 20, 15, 10]
count of 20: 1
index of 40: 2'''
