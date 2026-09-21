string = input("Enter a string: ")
ch = input("Enter a character: ")

first = string.find(ch)
last = string.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)


'''output:
Enter a string: apple
Enter a character: a
First occurrence: 0
Last occurrence: 0
'''
