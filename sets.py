import re

text = 'Residence dejection AGREEMENT'

pattern = re.compile(r'[A-Z ]')
matches = pattern.finditer(text)

for i in matches:
        print(i)

# advanced
text_2 = '''Domestic confined any but son bachelor advanced remember. 
        How proceed offered her offence shy forming. Returned peculiar 
        pleasant but appetite differed she dgottt@gmail.com. Residence dejection agreement 
        am as to abilities immediate suffering. Ye am depending propriety 
        sweetness distrusts belonging collected galena90@speeddataanalytics.com. Smiling mention he in 
        thought equally musical. Wisdom new and valley answer. Contented it 
        so is discourse recommend ievabaubinaite@oru-host.store. Man its upon him call mile. An pasture he 
        himself believe ferrars besides cottage.'''

# match emails

pattern_2 = re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.[a-z]+')
matches_2 = pattern_2.finditer(text_2)

for i in matches_2:
    print(i)
