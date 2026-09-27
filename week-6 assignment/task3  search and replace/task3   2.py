import re

names = input("Enter name: ")

result = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", names)

print(result)

'''output:
Enter name: Vakamulla, Sathish
Sathish Vakamulla'''
