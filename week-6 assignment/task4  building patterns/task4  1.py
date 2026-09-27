import re

pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"

names = input("Enter variable names separated by spaces: ").split()

for name in names:
    if re.fullmatch(pattern, name):
        print(name, "is valid")
    else:
        print(name, "is invalid")



'''output:
Enter variable names separated by spaces: _count2 2fast total_sum
_count2 is valid
2fast is invalid
total_sum is valid'''
