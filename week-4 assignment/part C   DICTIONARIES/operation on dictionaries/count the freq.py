text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)


'''output:
Enter a string: hello
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''
