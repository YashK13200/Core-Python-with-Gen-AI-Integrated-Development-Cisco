'''
L = []

def f1(a):
    return a+100


for var in [10,20,30,40,50]:
    r = f1(var)
    L.append(r)

>>> L
[110,120,130,140,150]

>>># map(function , collection) -> generator 

>>> map(lambda a: a+100, [10,20,30,40,50])
< map object at 0x....

>>> list(map(lambda a: a+100, [10,20,30,40,50]))
[110,120,130,140,150]

>>> list(map(lambda a: a> 25, [10,20,30,40,50]))     
[False, False, True, True, True]

>>> list(filter(lambda a: a> 25, [10,20,30,40,50]))
[30, 40, 50]



'''

