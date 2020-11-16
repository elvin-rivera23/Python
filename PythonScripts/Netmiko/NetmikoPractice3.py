"""

Created by: Elvin Rivera
Date: 11/16/2020

Description: Practice using Netmiko. Multi-vendor library to simplify Paramiko SSH connections to network devices


Note: Reference = https://github.com/ktbyers/netmiko

Practice3.png (configuring the access switches)
Switch 1 & 2 are acting as core switches in this topology 

3, 4 , 5 are access switches
"""


#!/usr/bin/env python

from netmiko import ConnectHandler

# Access Switch1
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'elvin',
    'password': 'cisco',
}

# Access Switch2
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'elvin',
    'password': 'cisco',
}

# Access Switch3
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'elvin',
    'password': 'cisco',
}

"""
open that file and each line will be read and split into a list.

"""
with open('iosv_l2_config1') as f:
    lines = f.read().splitlines()
print lines # print statement will show us the commands that will be applied to the switches

# connect to the device and then we're going to send configuration commands to the switches as specified by the list
all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 