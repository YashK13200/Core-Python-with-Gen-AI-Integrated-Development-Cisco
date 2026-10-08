# def fA(a):
#     return a.title()

# fA('bibu')
# # o/p -> 'Bibu'


# def fB(a):
#     if(a > 100 and a < 200):
#         return a+100
#     elif(a > 500 and a < 600):
#         return a+200
#     else:
#         return a+500
    
    
# # using lambda fB(arg)  
# L = []
# for var in [150,200,50,20,500,300]:
#     if(var > 200):
#         r = var + 100
#         L.append(r)
#     else:
#         r = var + 200
#         L.append(r)
# convert this python program to use lambda functions

fB = lambda a: a+100 if a > 200 else a+200
L = [fB(var) for var in [150,200,50,20,500,300]]
print(L)

# also do write in comprehension function style

L_comprehension = [var+100 if var > 200 else var+200 for var in [150,200,50,20,500,300]]
print(L_comprehension)
