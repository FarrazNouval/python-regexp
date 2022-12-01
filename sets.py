import re

text = 'Residence dejection AGREEMENT'

pattern = re.compile(r'[A-Z ]')
matches = pattern.finditer(text)

for i in matches:
    print(i)

