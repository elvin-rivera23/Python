"""

Created by: Elvin Rivera
Date: 11/12/2020

Description: Practice using Netmiko. Multi-vendor library to simplify Paramiko SSH connections to network devices


Note: Reference = https://github.com/ktbyers/netmiko

Different device types that it supports = https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py

"""

#!/usr/bin/env python

from netmiko import ConnectHandler

# specify name for the device and then device type
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'elvin',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2) #iosv layer 2 switch
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output

for n in range (2,21):
    print "Creating VLAN " + str(n)
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output 