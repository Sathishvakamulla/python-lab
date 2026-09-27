import re

text = "NASA and USA are working with ISRO on a new project."

matches = re.finditer(r"\b[A-Za-z]{7,}\b", text)

for match in matches:
    print(match.group(), match.start())

    '''output:
working 17
project 44
'''
