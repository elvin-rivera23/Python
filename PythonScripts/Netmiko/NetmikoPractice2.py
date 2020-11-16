"""

Created by: Elvin Rivera
Date: 11/16/2020

Description: Practice using Netmiko. Multi-vendor library to simplify Paramiko SSH connections to network devices


Note: Reference = https://github.com/ktbyers/netmiko

Different device types that it supports = https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py

"""


#!/usr/bin/env python

from netmiko import ConnectHandler

# configuration for switch 1
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'elvin',
    'password': 'cisco',
}

# configuration for switch 1
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'elvin',
    'password': 'cisco',
}

# configuration for switch 1
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'elvin',
    'password': 'cisco',
}

# variable that contains all of the above
all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

# create loop, connect to those switches, then subloop to create 20 VLANs
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print "Creating VLAN " + str(n)
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output 