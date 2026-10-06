'''
Write a python program:
1. create an empty dict
2. display no.of items - use len()
3. use - while loop - limit is 5
     - read hostname from <STDIN> (ex: host01)
     - read IP from <STDIN>    (ex: 10.20.30.40)
     - add input details(hostname,IP) to an existing dict
       dictName[New_Key] = Value

4. display no.of items
|
5. use for loop 
    - display hostname and IP
|
6. read a hostname from <STDIN>
7. test - input hostname is exists -> update IP 127.0.0.1
                |
                not
                |
                create a new hosts - 127.0.0.1 
|
8. display updated dict details.

'''
hosts = {}
print(f"No. of items in dictionary: {len(hosts)}")


count = 0
while count < 5:
    hostname = input("Enter hostname: ")
    ip = input("Enter IP: ")
    hosts[hostname] = ip
    # hosts.setdefault(hostname, ip) could be used to add the hostname and IP if it doesn't already exist
    count += 1

print(f"No. of items in dictionary: {len(hosts)}")

for var in hosts:
    print(f"Hostname:{var}\t IP Address:{hosts[var]}") # iterate through the dictionary and display each hostname and IP address

h = input("Enter a hostname:")
if h in hosts:
    hosts[h] = "127.0.0.1" # modify the IP address for the existing hostname 
else:
    print("sorry hostname {h} is not exists")
    hosts[h] = "127.0.0.1"
    print("Updated dict")

for var in hosts:
    print(f"\nHostname:{var}\t IP Address:{hosts[var]}") # iterate through the dictionary and display each hostname and IP address
    
    
