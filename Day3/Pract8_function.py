# function without parameters/arguments

def file_read():
    fobj = open('r1.log', 'r')
    s = fobj.read()
    fobj.close()
    print("file Contents:")
    print(s)
    print("End of the function block")
    
    
def calculate_sales_cost():
    total = 0
    for var in [10,20,30,40,50]:
        total += var
    print("Total sales cost:", total)
    
    
    
print("-- this is Main block") 
file_read()
print("")
calculate_sales_cost()
print("")

