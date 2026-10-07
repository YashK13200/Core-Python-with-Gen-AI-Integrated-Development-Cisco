import time

devices = ["switches", "routers", "firewalls", "access points", "ethernet"]

config = {'ID':'A-123', 'app':'demoApp', 'port':8080, 'fname':'/etc/app.cfg'}

wobj = open("r2.log", "w") # will create a new file if it doesn't exist or overwrite the existing file 
for var in devices:
    wobj.write(f"Device Name: {var}\n")
    
    
wobj.write("----------------Done-------------------------\n")


'''

'''
for var in config:
    wobj.write(f"{var}: {config[var]}\n")

wobj.write("----------------Done-------------------------\n")


wobj.write(f"Created on {time.ctime()}\n")

wobj.close()
