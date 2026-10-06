'''
Write a python program
i. Create an empty list 
2.Display number of elements in the list , use ln() function
| 
3.use while loop - limit is 5
-> read a hostname from user input
-> append the hostname to the list
4. Display number of elements in the list # use len() function # -> 5
|
5. use for loop -> iterate through the list

6. read a hostname from <STDIN>
7. test input hostname is existing or not in the list
                            |         ================
  8.                          modify the hostname    |_ Add the Hostname
  9. display the list of hostnames - use for loop 
'''
hostnames = []

print(f"Number of elements in the list: {len(hostnames)}")

count = 0
while count < 5:
    hostname = input("Enter a hostname: ")
    hostnames.append(hostname)
    count += 1

print(f"Number of elements in the list: {len(hostnames)}")

for hostname in hostnames:
    print(hostname)

hostname_to_check = input("Enter a hostname to check: ")
if hostname_to_check in hostnames:
    hostnames[-1] = hostname_to_check
else:
    hostnames.append(hostname_to_check)

print("\n")

print("Updated list of hostnames:")
for hostname in hostnames:
    print(hostname)
