import re

text = input("Enter text: ")

pattern = r"\(?(\d{3})\)?[-. ](\d{3})[-. ](\d{4})"

numbers = re.findall(pattern, text)

for number in numbers:
    phone = re.sub(pattern, r"\1-\2-\3", "-".join(number))
    print(phone)



'''output:
Enter text: Contact 555-123-4567 or (555) 987-6543 or 555.456.7890
555-123-4567
555-987-6543
555-456-7890'''
