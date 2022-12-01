# regex

# 1. methods to search for matches [finditer(), findall(), match(), search]

import re

text = '''Domestic confined any but son bachelor advanced remember. 
        How proceed offered her offence shy forming. Returned peculiar 
        pleasant but appetite differed she. Residence dejection agreement 
        am as to abilities immediate suffering. Ye am depending propriety 
        sweetness distrusts belonging collected. Smiling mention he in 
        thought equally musical. Wisdom new and valley answer. Contented it 
        so is discourse recommend. Man its upon him call mile. An pasture he 
        himself believe ferrars besides cottage.'''

pattern = re.compile(r'so')
matches_1 = pattern.finditer(text)  # returns callable match object
matches_2 = pattern.findall(text)  # returns all strings that match the pattern
matches_3 = pattern.match(text)  # only returns match on the begining of the text
matches_4 = pattern.search(text) # only returns first match object

for match in matches_1:
    print(f'find iter method output => {match}')

for match in matches_2:
    print(f'find all method output => {match}')

print(f'match method output => {matches_3}')

print(f'search method output => {matches_4}')

# methods on match object
# group, span, end, start

for match in matches_1:
    print(f'output of finditer => {match}')
    print(f'output of group method => {match.group()}')
    print(f'output of span method => {match.span()}')
    print(f'output of end method => {match.end()}')
    print(f'output of start method => {match.start()}')
