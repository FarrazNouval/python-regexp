import re

text = '''Domestic confined any but son bachelor advanced remember. 
        How proceed offered her offence shy forming. Returned peculiar 
        pleasant but appetite differed she dgottt@gmail.com. Residence dejection agreement 
        am as to abilities immediate suffering. Ye am depending propriety 
        sweetness distrusts belonging collected galena90@speeddataanalytics.com. Smiling mention he in 
        thought equally musical. Wisdom new and valley answer. Contented it 
        so is discourse recommend ievabaubinaite@oru-host.store. Man its upon him call mile. An pasture he 
        himself believe ferrars besides cottage.'''

# match emails

pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-z]+)')
matches = pattern.finditer(text)

for i in matches:
    print(i.group(0))  # dgottt@gmail.com ---> the entire text that matches the pattern
    print(i.group(1))  # dgottt ---> 1st group from group(0) ([a-zA-Z0-9-]+)
    print(i.group(2))  # gmail ---> 2nd group from group(0) ([a-zA-Z-]+)
    print(i.group(3))  # com ---> 3rd group from group(0) ([a-z]+)

# .group(0) returns the entire text that match the pattern
# .group(n) returns the text that match the nth pattern group
