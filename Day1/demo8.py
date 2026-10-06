'''
Write a python program:
-> Read an App Name from <STDIN>
-> test - flask -> Initialize port number is 5000
->test - fastAPI -> initialize port number is 8080
-> test - Prometheus -> Initialize port number is 9090

- default app name is : web2.0 and port number 8000
- display app name and running port number
'''

app_name = input("Enter App Name: ")
# using Conditional Statement with ==
if app_name.lower() == 'flask':
    port = 5000
elif app_name.lower() == 'fastapi':
    port = 8080
elif app_name.lower() == 'prometheus':
    port = 9090
else:
    app_name = "web2.0"
    port = 8000

print(f"App Name is: {app_name} Running Port Number is: {port}")
