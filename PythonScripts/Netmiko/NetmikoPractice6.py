"""

Created by: Elvin Rivera
Date: 11/16/2020

Description: Practice using Netmiko. Multi-vendor library to simplify Paramiko SSH connections to network devices

Designing for Campus Wired LAN (Technology Design Guide)

Note: Reference = https://www.cisco.com/c/dam/en/us/td/docs/solutions/CVD/Aug2014/CVD-CampusWiredLANDesignGuide-AUG14.pdf

Same topology as Practice3.PNG
"""


#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'elvin',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'elvin',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'elvin',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.74',
    'username': 'elvin',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'elvin',
    'password': 'cisco',
}

# applying this to access switches
with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 

# applying this to core switches
with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 