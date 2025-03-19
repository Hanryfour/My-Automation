# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | borderleaf1 | 192.168.0.28/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | borderleaf2 | 192.168.0.29/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf1 | 192.168.0.20/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf2 | 192.168.0.21/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf3 | 192.168.0.22/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf4 | 192.168.0.23/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | spine1 | 192.168.0.24/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | spine2 | 192.168.0.25/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | spine3 | 192.168.0.26/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | spine4 | 192.168.0.27/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | borderleaf1 | Ethernet1 | mlag_peer | borderleaf2 | Ethernet1 |
| l3leaf | borderleaf1 | Ethernet2 | mlag_peer | borderleaf2 | Ethernet2 |
| l3leaf | borderleaf1 | Ethernet3 | spine | spine1 | Ethernet7 |
| l3leaf | borderleaf1 | Ethernet4 | spine | spine2 | Ethernet7 |
| l3leaf | borderleaf1 | Ethernet5 | spine | spine3 | Ethernet7 |
| l3leaf | borderleaf1 | Ethernet6 | spine | spine4 | Ethernet7 |
| l3leaf | borderleaf2 | Ethernet3 | spine | spine1 | Ethernet8 |
| l3leaf | borderleaf2 | Ethernet4 | spine | spine2 | Ethernet8 |
| l3leaf | borderleaf2 | Ethernet5 | spine | spine3 | Ethernet8 |
| l3leaf | borderleaf2 | Ethernet6 | spine | spine4 | Ethernet8 |
| l3leaf | leaf1 | Ethernet1 | mlag_peer | leaf2 | Ethernet1 |
| l3leaf | leaf1 | Ethernet2 | mlag_peer | leaf2 | Ethernet2 |
| l3leaf | leaf1 | Ethernet3 | spine | spine1 | Ethernet3 |
| l3leaf | leaf1 | Ethernet4 | spine | spine2 | Ethernet3 |
| l3leaf | leaf1 | Ethernet5 | spine | spine3 | Ethernet3 |
| l3leaf | leaf1 | Ethernet6 | spine | spine4 | Ethernet3 |
| l3leaf | leaf2 | Ethernet3 | spine | spine1 | Ethernet4 |
| l3leaf | leaf2 | Ethernet4 | spine | spine2 | Ethernet4 |
| l3leaf | leaf2 | Ethernet5 | spine | spine3 | Ethernet4 |
| l3leaf | leaf2 | Ethernet6 | spine | spine4 | Ethernet4 |
| l3leaf | leaf3 | Ethernet1 | mlag_peer | leaf4 | Ethernet1 |
| l3leaf | leaf3 | Ethernet2 | mlag_peer | leaf4 | Ethernet2 |
| l3leaf | leaf3 | Ethernet3 | spine | spine1 | Ethernet5 |
| l3leaf | leaf3 | Ethernet4 | spine | spine2 | Ethernet5 |
| l3leaf | leaf3 | Ethernet5 | spine | spine3 | Ethernet5 |
| l3leaf | leaf3 | Ethernet6 | spine | spine4 | Ethernet5 |
| l3leaf | leaf4 | Ethernet3 | spine | spine1 | Ethernet6 |
| l3leaf | leaf4 | Ethernet4 | spine | spine2 | Ethernet6 |
| l3leaf | leaf4 | Ethernet5 | spine | spine3 | Ethernet6 |
| l3leaf | leaf4 | Ethernet6 | spine | spine4 | Ethernet6 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.34.1.0/24 | 256 | 48 | 18.75 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| borderleaf1 | Ethernet3 | 10.34.1.161/31 | spine1 | Ethernet7 | 10.34.1.160/31 |
| borderleaf1 | Ethernet4 | 10.34.1.163/31 | spine2 | Ethernet7 | 10.34.1.162/31 |
| borderleaf1 | Ethernet5 | 10.34.1.165/31 | spine3 | Ethernet7 | 10.34.1.164/31 |
| borderleaf1 | Ethernet6 | 10.34.1.167/31 | spine4 | Ethernet7 | 10.34.1.166/31 |
| borderleaf2 | Ethernet3 | 10.34.1.169/31 | spine1 | Ethernet8 | 10.34.1.168/31 |
| borderleaf2 | Ethernet4 | 10.34.1.171/31 | spine2 | Ethernet8 | 10.34.1.170/31 |
| borderleaf2 | Ethernet5 | 10.34.1.173/31 | spine3 | Ethernet8 | 10.34.1.172/31 |
| borderleaf2 | Ethernet6 | 10.34.1.175/31 | spine4 | Ethernet8 | 10.34.1.174/31 |
| leaf1 | Ethernet3 | 10.34.1.1/31 | spine1 | Ethernet3 | 10.34.1.0/31 |
| leaf1 | Ethernet4 | 10.34.1.3/31 | spine2 | Ethernet3 | 10.34.1.2/31 |
| leaf1 | Ethernet5 | 10.34.1.5/31 | spine3 | Ethernet3 | 10.34.1.4/31 |
| leaf1 | Ethernet6 | 10.34.1.7/31 | spine4 | Ethernet3 | 10.34.1.6/31 |
| leaf2 | Ethernet3 | 10.34.1.9/31 | spine1 | Ethernet4 | 10.34.1.8/31 |
| leaf2 | Ethernet4 | 10.34.1.11/31 | spine2 | Ethernet4 | 10.34.1.10/31 |
| leaf2 | Ethernet5 | 10.34.1.13/31 | spine3 | Ethernet4 | 10.34.1.12/31 |
| leaf2 | Ethernet6 | 10.34.1.15/31 | spine4 | Ethernet4 | 10.34.1.14/31 |
| leaf3 | Ethernet3 | 10.34.1.17/31 | spine1 | Ethernet5 | 10.34.1.16/31 |
| leaf3 | Ethernet4 | 10.34.1.19/31 | spine2 | Ethernet5 | 10.34.1.18/31 |
| leaf3 | Ethernet5 | 10.34.1.21/31 | spine3 | Ethernet5 | 10.34.1.20/31 |
| leaf3 | Ethernet6 | 10.34.1.23/31 | spine4 | Ethernet5 | 10.34.1.22/31 |
| leaf4 | Ethernet3 | 10.34.1.25/31 | spine1 | Ethernet6 | 10.34.1.24/31 |
| leaf4 | Ethernet4 | 10.34.1.27/31 | spine2 | Ethernet6 | 10.34.1.26/31 |
| leaf4 | Ethernet5 | 10.34.1.29/31 | spine3 | Ethernet6 | 10.34.1.28/31 |
| leaf4 | Ethernet6 | 10.34.1.31/31 | spine4 | Ethernet6 | 10.34.1.30/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.10.4.0/24 | 256 | 6 | 2.35 % |
| 192.168.101.0/24 | 256 | 4 | 1.57 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | borderleaf1 | 10.10.4.21/32 |
| FABRIC | borderleaf2 | 10.10.4.22/32 |
| FABRIC | leaf1 | 10.10.4.1/32 |
| FABRIC | leaf2 | 10.10.4.2/32 |
| FABRIC | leaf3 | 10.10.4.3/32 |
| FABRIC | leaf4 | 10.10.4.4/32 |
| FABRIC | spine1 | 192.168.101.11/32 |
| FABRIC | spine2 | 192.168.101.12/32 |
| FABRIC | spine3 | 192.168.101.13/32 |
| FABRIC | spine4 | 192.168.101.14/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 172.16.1.0/24 | 256 | 6 | 2.35 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | borderleaf1 | 172.16.1.21/32 |
| FABRIC | borderleaf2 | 172.16.1.21/32 |
| FABRIC | leaf1 | 172.16.1.1/32 |
| FABRIC | leaf2 | 172.16.1.1/32 |
| FABRIC | leaf3 | 172.16.1.3/32 |
| FABRIC | leaf4 | 172.16.1.3/32 |
