'''
write a python program
to Demonstrate - ATM pin Number Validation
use while loop
 - limit is 3 attempts
 - read a input pin from <STDIN>
 -test - if pin is corrrect -> display "Pin number is Valid" - Display Count
 - if all 3 attempts are failed -> display "Pin number is Blocked"
'''

pin = "1234"
count = 0

while count < 3:
    user_pin = int(input("Enter your ATM pin Number: "))
    if user_pin == pin:
        print(f"Pin number is Valid - Attempt {count + 1}")
        break
    else:
        count += 1
        if count == 3:
            print("Pin number is Blocked")
