
import re

text = input("Enter text: ")

def hide_email(match):
    return "[EMAIL HIDDEN]"

result = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', hide_email, text)

print(result)

'''output:
Enter text: Sathish email is sathish@gmail.com and college email is sathish123@gmail.com
Sathish email is [EMAIL HIDDEN] and college email is [EMAIL HIDDEN]'''
