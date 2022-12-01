import re

text = '''
Mr Aaa
Mrs. Bbb
Ms. Ccc
Mr Ddd
Mr. Eee
Ms. Fff
Mrs. Ggg'''

# pattern with conditional
# Mr followed or not followed by dot and then space and followed by alphanumeric that occurs at least once
pattern = re.compile(r'Mr\.?\s\w+')
matches = pattern.finditer(text)

for i in matches:
    print(i)

# Mr followed by dot or whitespace and followed by alphanumeric that occurs at least once
pattern_2 = re.compile(r'Mr(\.|)\s\w+')
matches_2 = pattern_2.finditer(text)

for i in matches_2:
    print(i)
