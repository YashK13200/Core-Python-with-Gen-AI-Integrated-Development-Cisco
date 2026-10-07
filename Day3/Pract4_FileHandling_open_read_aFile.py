# open a file and read its contents into a list of lines

fobj = open('C:/Users/Admin/Documents/Py Training/Day-1/emp.csv', 'r')
L = fobj.readlines()

fobj.close()

for var in L:
    print(var.strip()) # strip() removes leading and trailing whitespace characters, including newline characters
    
# splitting each data 
print("\n") 

for var in L:
    if 'sales' in var:
        var = var.strip()  # split the line into a list of values based on comma
        print(var)

   
print("\n")

for var in L:
    var = var.strip()  # split the line into a list of values based on comma
    eid, ename, edept ,eplace , ecost, = var.split(',')
    total = total + int(ecost)
    print(f"Emp Name is : {ename.title()}, \t Working Dept is : {edept.upper()}")
    
print("-"*35)
print(f"Sum of sales emp's dept is: {total}")   
print("-"*35)
    
