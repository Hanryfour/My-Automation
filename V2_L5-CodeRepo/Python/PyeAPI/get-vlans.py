import yaml
import pyeapi

file = open('leafs.yml','r')
data_raw = file.read()
data_model = yaml.safe_load(data_raw)
for switch,leafs in data_model.items():
    print(leafs)
    for leaf in leafs:
        print(leaf)
        test = pyeapi.load_config('/home/automation-Lab/arista-Lab/my-git-lab/My-Automation/V2_L5-CodeRepo/Python/PyeAPI/eapi.conf')
        connect = pyeapi.connect_to(leaf)
        print(connect)
        api_vlan = connect.api('vlans')
        vlans = api_vlan.getall()
        vlans_set = set()
        for vlan in vlans:
            vlans_set.add(vlan)
        print(f" the vlan on {switch} are {vlans_set}")