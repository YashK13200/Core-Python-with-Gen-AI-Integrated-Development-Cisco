fobj = open('C:/Users/Admin/Documents/Py Training/Day-1/emp.csv', 'r')

L = fobj.readlines()
fobj.close()

total = 0
for var in L:
    if 'sales' in var:
        var = var.strip()
        emp_list = var.split(',')
        ecost = emp_list[-1]
        total = total + int(ecost)
print(f"Sum of Sales dept emp's cost {total}")        


'''
# in Functional Programming 

>>> fobj = open('C:/Users/Admin/Documents/Py Training/Day-1/emp.csv', 'r')

>>> map(lambda a:a, open('C:/Users/Admin/Documents/Py Training/Day-1/emp.csv', 'r')))




>>> P1 = list(map(lambda a:a, open('C:/Users/Admin/Documents/Py Training/Day-1/emp.csv', 'r')))
>>> list(filter(lambda a: 'sales' in a, P1))


>>> P1 = list(map(lambda a:a, open('C:/Users/Admin/Documents/Py Training/Day-1/emp.csv', 'r')))
>>> P2 = list(filter(lambda a:'sales' in a,P1))
>>>
>>> P3 = list(map(lambda a:a.split(",")[-1],P2))
>>> P3
['1000\n', '3401\n', '5419\n', '5901\n']
>>>
>>> functools.reduce(lambda a,b:int(a)+int(b),P3)
15721
>>>
>>> functools.reduce(lambda a,b:int(a)+int(b),map(lambda a:a.split(",")[-1],filter(lambda a:'sales' in a,map(lambda a:a,open('emp.csv','r'))))
... )
15721
>>>


'''
# python functional programming with Same logic of the above code starting from line number 19

import functools

fobj = open('C:/Users/Admin/Documents/Py Training/Day-1/emp.csv', 'r')
D = fobj.readlines()
fobj.close()

total = functools.reduce(lambda a,b:int(a)+int(b),map(lambda a:a.split(",")[-1],filter(lambda a:'sales' in a,D)))
print(f"Sum of Sales dept emp's cost {total}")  

# The above code reads the employee data from the CSV file, filters out the sales department employees, extracts their costs, and calculates the total using functional programming with map, filter, and reduce functions.
    
