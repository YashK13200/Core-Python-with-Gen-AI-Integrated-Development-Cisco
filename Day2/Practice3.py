'''
given List
Emp = ['101,john, sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

-> iterate the emp list
-> split each element of the list using ',' as a delimiter
-> filter the sales department employees
-> display empName in title case and empt deptartment in upper case 
-> calculate sum of salary of sales department emp salary and display the total salary
 
'''
Emp = ['101,john, sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

total_Sales_salary = 0

for var in Emp:
    if 'sales' in var:
        eid, ename, edept, esalary = var.split(',')
        print(f"Employee Name: {ename.title()}, Department: {edept.upper()}")
        total_Sales_salary += int(esalary)

print(f"Total Salary: {total_Sales_salary}")
