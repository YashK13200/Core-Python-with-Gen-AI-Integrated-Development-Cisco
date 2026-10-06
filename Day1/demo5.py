''' write a Python program 
 read employee details(name , age , cost , login_status) from user input
 using print() - display the employee details
'''

elogin_status = True

ename = input("Enter employee name: ")

eage = input(f"Enter {ename} age: ")

ecost = input(f"Enter {ename} Basic Salary: ")

tax = float(ecost) * 0.18
gs = tax + float(ecost)


print(f'''Employee name : {ename}
------------------------------------
{ename} Age is : {eage}
------------------------------------
{ename} Basic Salary is : {ecost}
------------------------------------
{ename} Login status is : {elogin_status}
------------------------------------
{ename} Tax is : {tax}
------------------------------------
{ename} Total Salary is : {gs}
------------------------------------
''')

