import re

text = input("Enter a sentence: ")

result, count = re.subn(r"([!?.,])\1+", r"\1", text)

print(result)
print("Replacements:", count)





''''output:
Enter a sentence: Sathish is coming!!! Wait!!! Are you ready??
Sathish is coming! Wait! Are you ready?
Replacements: 2''''
