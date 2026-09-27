import re

s1 = "12345"
s2 = "123a5"

print(re.fullmatch(r"\d+", s1))
print(re.fullmatch(r"\d+", s2))


'''output:
<re.Match object; span=(0, 5), match='12345'>
None
'''
