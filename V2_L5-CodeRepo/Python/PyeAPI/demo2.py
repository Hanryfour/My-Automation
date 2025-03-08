import yaml
import pyeapi
#open example.yml with read permission 
file = open('example.yml','r')
#read method will read the content of the file 
data_model_raw = file.read()
#load the content file in yml dictionary 
data_model = yaml.safe_load(data_model_raw)
#print(data_model)
# for switches in data_model:
#     print(f"connecting to {switches}")
#     switch = data_model[switches]
#     #print(switch)
#     for interface,address in switch.items():
#         print(f"interface {interface}")
#         print(' no switchport')
#         print(f" ip address {address}")
#         print (' no shut')
# print (data_model)
for switches,port in data_model.items():
    print (f"connnecting to {switches}")
    print (f"configuring  {switches}")
    # print(port)
    for interface, ip in port.items():
        print(f"inteface {interface}")
        print (f" no switchport")
        print(f" ip address {ip}")
        print (' no shut')
    test = pyeapi.load_config('/home/automation-Lab/arista-Lab/my-git-lab/My-Automation/V2_L5-CodeRepo/Python/PyeAPI/eapi.conf')
    connect = pyeapi.connect_to(switches)
    api_vlan = connect.api('vlans')
    vlans = api_vlan.getall()
    vlans_set = set()
    for vlan in vlans:
        vlans_set.add(vlan)
    print(f" the vlan on {switches} are {vlans_set}")