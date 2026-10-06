'''
Write a python program:
-> Read a AppName from <STDIN>
-> test - using membership test flask is running -> port = 5000
                                |__ not running -> port = 8080

-> Display - app name and running port Number
'''

app_name = input("Enter App Name: ")
if 'flask' in app_name.lower():
    port = 5000
else:
    port = 8080

print(f"App Name is: {app_name} Running Port Number is: {port}")
