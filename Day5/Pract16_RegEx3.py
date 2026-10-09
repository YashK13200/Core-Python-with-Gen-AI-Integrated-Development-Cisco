'''
s = ['120GB','500GB','GB200','150Gb','300gb',400]
calculate sum of the size - display total size
write python program to handle different cases of GB and sum them correctly
'''

# s = '120GB' 
# >>> re.findall('[A-Za-z]', s)
#>>> ['G', 'B']
#
# >>> re.sub('[A-Za-z]', '', s)
# >>> '120'
# Use these logics and similar to Write Code

import re

total_size = 0  

s = ['120GB','500GB','GB200','150Gb','300gb','400']

for var in s:
    size = re.sub('[A-Za-z]', '', var)
    total_size = total_size + int(size)
    
print(f"Sum of {s} disk size: {total_size}GB\n")    

print([int(re.sub('[A-Za-z]', '', var)) for var in s]) # list of comprehension
