'''
Write a python program:
--> read a port Number form <STDIN>

-> Test - input port number range is 5001-5999
          -------------------------------------
            |--> initialize app name is Flask
     |-->initialize app name is WebApp

--> Display - App Name and Running port Number
'''
port = input("Enter port number: ")

if int(port) > 5000 and int(port) < 6000:
    app_name = "Flask"
else:
    app_name = "WebApp"

print(f"App Name is:{app_name} Running Port Number is:{port}")
