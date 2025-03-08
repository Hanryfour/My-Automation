ip = {'E1':'10.1.1.1','E2':'10.1.2.2','E3':'10.1.3.3'}
print(ip)
for interface in ip:
    print(f"interface  {interface}")
    print('no switchport')
    print(f"ip address {ip[interface]}")
    print('no shut')
#or using items which allow us to split the variable into two and return both key and value 
for interface,address in ip.items():
    print(interface)
    print (address)