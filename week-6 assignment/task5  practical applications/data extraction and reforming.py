import re

text = input("Enter text: ")

pattern = r"(\d{2})/(\d{2})/(\d{4})"

dates = re.findall(pattern, text)

print("Extracted dates:", dates)

result = re.sub(pattern, r"\3-\2-\1", text)

print("Reformatted text:", result)


'''output:
Enter text: My birthday is 15/08/2006 and my admission date is 20/06/2024.
Extracted dates: [('15', '08', '2006'), ('20', '06', '2024')]
Reformatted text: My birthday is 2006-08-15 and my admission date is 2024-06-20.'''
