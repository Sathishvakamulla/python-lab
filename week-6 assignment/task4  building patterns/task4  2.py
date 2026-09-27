import re

text = input("Enter a sentence: ")

pattern = r"\b(cat|dog|bird)\b"

result = re.findall(pattern, text)

print(result)


'''output:
Enter a sentence: I have a cat and a dog, and my friend has a bird.
['cat', 'dog', 'bird']'''
