'''
write a Python program:
initilaize employee details(name , age , cost , login_status)
to variables

using print() - display the employee details

Expected Output :
Employee name : John Doe
Employee age : 30
Employee cost : 50000.0
Employee login status : True
'''

Ename = "John Doe"
Eage = 30
Ecost = 50000.0
Elogin_status = True

print(f'Employee name : {Ename}')
print(f'Employee age : {Eage}')
print(f'Employee cost : {Ecost}')
print(f'Employee login status : {Elogin_status}')

print("\n") 
print("\n") 

# print same thing again using multiline string
print(f'''Employee name : {Ename}
------------------------------------      
Employee age : {Eage}
------------------------------------
Employee cost : {Ecost}
------------------------------------
Employee login status : {Elogin_status}
------------------------------------''')
