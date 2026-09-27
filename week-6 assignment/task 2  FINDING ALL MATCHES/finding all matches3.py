
import re

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r'\$\d+\.\d+', prices)

print(amounts)


**Output:**


['$3.50', '$1.20', '$4.75']



'''output:
['$3.50', '$1.20', '$4.75']'''
