import re

sentence = "1024 requests were served in 3 seconds"

if re.match(r"\d", sentence):
    print("Sentence starts with a digit")
else:
    print("Sentence does not start with a digit")
