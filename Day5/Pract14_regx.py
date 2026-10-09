import re
fobj = open("r1.log", "r")
for var in fobj:
    if re.search(r"ERROR", var):
        print(var)
fobj.close()

