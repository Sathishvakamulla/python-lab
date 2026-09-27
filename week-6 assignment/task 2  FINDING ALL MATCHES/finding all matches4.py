
import re

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r'\$\d+\.\d+', prices)

print(amounts)
print("Count:", len(amounts))


**Output:**


['$3.50', '$1.20', '$4.75']
Count: 3


'''output:
Enter prices: apples: $3.50, bananas: $1.20, mango: $4.75
['$3.50', '$1.20', '$4.75']
Count: 3'''
