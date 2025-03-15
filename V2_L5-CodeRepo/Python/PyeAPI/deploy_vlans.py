import yaml
import pyeapi

file = open('vlans.yml', 'r')
pyeapi.load_config('/home/automation-Lab/arista-Lab/my-git-lab/My-Automation/V2_L5-CodeRepo/Python/PyeAPI/eapi.conf')
vlan_dict = yaml.safe_load(file)
# print(vlan_dict)

for switch in vlan_dict['switches']:
    print(f" connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan ['name']
        print(f" adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id,vlan_name)
    

