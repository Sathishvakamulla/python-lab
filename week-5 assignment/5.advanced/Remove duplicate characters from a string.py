string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)



''' output:
Enter a string: sathish
After removing duplicates: sathi'''
