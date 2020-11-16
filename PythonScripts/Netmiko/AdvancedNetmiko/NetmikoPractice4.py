"""

Created by: Elvin Rivera
Date: 11/16/2020

Description: Practice using Netmiko. Multi-vendor library to simplify Paramiko SSH connections to network devices


Note: Reference = https://github.com/ktbyers/netmiko

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

# Open access switch file
with open('iosv_l2_access') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 

# Open core switch file
with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 