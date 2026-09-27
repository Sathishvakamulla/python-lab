import re

def is_valid_email(s):
    pattern = r"^[\w.]+@[\w.-]+\.[A-Za-z]{2,6}$"
    return bool(re.fullmatch(pattern, s))

emails = input("Enter email addresses separated by spaces: ").split()

for email in emails:
    print(email, "->", is_valid_email(email))


'''output:
Enter email addresses separated by spaces: sathish@gmail.com sathish.v@gmail.com a@b.c no-at-sign.com test@gmail.com abc@domain.co 123@abc.com abc@@gmail.com
sathish@gmail.com -> True
sathish.v@gmail.com -> True
a@b.c -> False
no-at-sign.com -> False
test@gmail.com -> True
abc@domain.co -> True
123@abc.com -> True
abc@@gmail.com -> False'''
