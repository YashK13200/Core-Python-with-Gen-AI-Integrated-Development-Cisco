'''
there are mainly four function type with arguments:
1. required arguments def f1(a1, a2,......an)
2. default arguments def f2(a1, a2=10,......an=20)
3. variable-length arguments def f4(*args)
4. keyword arguments def f3(**a)

Write a python program in which we have to do following tasks:
1. Modify ATM pin test
-> create a pin_history.log file - append mode

-> use ATM pin number validation - maximum limit is 3
   -> valid PIN -> update pin details to pin_history.log
                          ------------
                           Success - <count> + Date/Time <= time.ctime()
                           
    -> Invalid PIN -> u[date - user_input_pin + date/Time to pin_hostory.log file 
    
   -> pin is blocked 
      -> update to pin_hostory.log file + Date/Time
      
2. Create a new function - pin_test(pin)                                  
'''

import time
def pin_test():
    fobj = open("pin_history.log", "a")
    pin = 1234
    count = 0
    while(count < 3):
        p = input("Enter your PIN: ")
        count += 1
        if(int(p) == pin):
            print(f"Success - {count}")
            fobj.write(f"Success - {count} + pin input Date/Time: {time.ctime()}\n")
            break
        else:
            fobj.write(f"Failed - user input pin - {p} + pin input Date/Time: {time.ctime()}\n")
        
    if(int(p) != pin):
        print("PIN is blocked")
        fobj.write(f"PIN is blocked + Date/Time: {time.ctime()}\n")
        fobj.close()



pin_test()

