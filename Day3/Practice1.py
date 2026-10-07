'''
L=[(101,'ram','sales',1000),(102,'leo','sales',2000),(103,'bibu','prod',3000)]
Update - Leo emp cost -> 5000
Add - new emp records (104,theeb,HR,4000) to an existing list
'''
L=[(101,'ram','sales',1000),(102,'leo','sales',2000),(103,'bibu','prod',3000)]

L[1] = (102,'leo','sales',5000)
L.append((104,'theeb','HR',4000))
print(L)
