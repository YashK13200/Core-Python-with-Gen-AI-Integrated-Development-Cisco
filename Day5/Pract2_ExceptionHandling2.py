import sys

try:
    fobj = open('invalidFile', 'r')
except PermissionError as eobj:
    print("This is 1st Except Block")
    print(eobj)
except FileNotFoundError as eobj:
    print("This is 2nd Except Block")
    print(eobj)
    
    
#Vs

try:
    fobj = open('invalidFile', 'r')
except Exception as eobj:
    print(eobj)

print("")

#Vs
try:
    fobj = open('invalidFile', 'r')
except Exception:
    print(sys.exc_info())
