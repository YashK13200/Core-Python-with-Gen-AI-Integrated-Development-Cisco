'''
write a python program to read from 'inputFile' and write its contents to 'resultFile'
fobj = open('r1.log', 'r') 
wobj = open('r3.log', 'w')

s = fobj.read()
wobj.write(s)
fobj.close()
wobj.close()
'''

fobj = open('r1.log', 'r') 
wobj = open('r3.log', 'w')

s = fobj.read()
wobj.write(s)
fobj.close()
wobj.close()


#### Vs using with as keywords - contextmanager

with open('r1.log','r') as fobj:
    with open('r4.log', 'w') as wobj:
        L = fobj.readlines()
        for var in L:
            wobj.write(f"data -> {var}")
            
            
            
print("End of the line")            
