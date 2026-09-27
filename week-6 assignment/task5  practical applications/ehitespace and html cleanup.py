import re

def clean_text(html):
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

html = input("Enter HTML text: ")

print(clean_text(html))

'''output:
Enter HTML text: <p>Hello   Sathish</p>   <b>Welcome</b>   to <i>Python</i>
Hello Sathish Welcome to Python'''
