wobj = open("r1.log", "w") # will create a new file if it doesn't exist or overwrite the existing file 
# here we haven't given file path so the file r1.log will be created in the current working directory
wobj.write("This is a test log entry.\n")
wobj.write("Product name is:Pa Cost is:4556\n")

print("\n")

pname = "Pb"
pcost = 3556.23
wobj.write(f"Product name is:{pname} Cost is:{pcost}\n")
wobj.write("-----------------------------------------\n")


wobj.close()
