'''
given List
Emp = ['101,john, sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

-> iterate the emp list
-> split each element of the list using ',' as a delimiter
-> display empName in title case and empt deptartment in upper case 
-> calculate sum of emp salary and display the total salary
 
'''
Emp = ['101,john, sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

total_salary = 0
for emp in Emp:
    emp_details = emp.split(',')
    emp_id = emp_details[0]
    emp_name = emp_details[1].title()
    emp_dept = emp_details[2].upper()
    emp_salary = int(emp_details[3])
    total_salary += emp_salary
    print(f"Employee Name: {emp_name}, Department: {emp_dept}")

print(f"Total Salary: {total_salary}")
