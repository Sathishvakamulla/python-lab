def to_upper(s):
    return s.upper()

strings = []

n = int(input("Enter number of strings: "))

for i in range(n):
    s = input("Enter string: ")
    strings.append(s)

uppercase = list(map(to_upper, strings))

print("Uppercase strings:", uppercase)



''' output:
Enter number of strings: 3
Enter string: hello
Enter string: python
Enter string: world
Uppercase strings: ['HELLO', 'PYTHON', 'WORLD']'''
