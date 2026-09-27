strings = []

n = int(input("Enter number of strings: "))

for i in range(n):
    s = input("Enter string: ")
    strings.append(s)

sorted_strings = sorted(strings, key=lambda s: len(s))

print("Strings sorted by length:")
for s in sorted_strings:
    print(s)

'''output:
Enter number of strings: 5
Enter string: Python
Enter string: AI
Enter string: Programming
Enter string: Code
Enter string: Data

Strings sorted by length:
AI
Code
Data
Python
Programming'''
