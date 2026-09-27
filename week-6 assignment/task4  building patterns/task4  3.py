import re

text = input("Enter color codes: ")

pattern = r"#[A-Fa-f0-9]{3}(?:[A-Fa-f0-9]{3})?"

result = re.findall(pattern, text)

print(result)


'''output:
Enter color codes: #FFAA00 #000 #12ABCD #FFF
['#FFAA00', '#000', '#12ABCD', '#FFF']'''
