import re

text = "NASA and USA are working with ISRO on a new project."

words = re.findall(r"\b[A-Z]{2,}\b", text)

print(words)


'''output:
['NASA', 'USA', 'ISRO']'''
