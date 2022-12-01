import re

text = 'Residence_dejection 1234'

pattern = re.compile(r'_?\d{4}')
matches = pattern.finditer(text)

# for i in matches:
#     print(i)

dates = '''
19.07.2020
20.07.2020
21.07.2020
22.07.2020

19/07/2020
20/07/2020
21/07/2020
22/07/2020

19-07-2020
20-07-2020
21-07-2020
22-07-2020'''

pattern_2 = re.compile(r'\d{2}[-/]\d{2}[-/]\d{4}')
matches_2 = re.finditer(pattern_2, dates)

for i in matches_2:
    print(i)
