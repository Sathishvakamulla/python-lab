import re

sentence = "1024 requests were served in 3 seconds"

match = re.search(r"served", sentence)

if match:
    print("Start and end position:", match.span())


'''output:
Start and end position: (19, 25)
'''
    
