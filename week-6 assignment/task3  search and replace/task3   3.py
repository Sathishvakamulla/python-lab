import re

text = input("Enter a sentence: ")

def double_number(match):
    return str(int(match.group()) * 2)

result = re.sub(r"\d+", double_number, text)

print(result)


'''output:
Enter a sentence: Sathish has 3 apples and 5 bananas
Sathish has 6 apples and 10 bananas'''
