"""

Created by: Elvin Rivera
Date: 11/12/2020

Description: Practice using Paramiko and SSH (Paramiko is a module). This is to use SSH rather than TelNet


Note: Reference = https://www.paramiko.org/

This is Ubuntu Client based

Ubuntu machine is configured to use DHCP
"""


import paramiko
import time

ip_address = "192.168.122.72"
username = "elvin"
password = "cisco"

# uses ssh to connect and configure some options on the switch
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #paramiko rejects unknown ssh keys, just accepting putblic key. DONT DO THIS IN PRODUCTION
ssh_client.connect(hostname=ip_address,username=username,password=password) 

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

# Configure some loopback interfaces & loop to configure VLAN on switch
remote_connection.send("configure terminal\n")
remote_connection.send("int loop 0\n")
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")
remote_connection.send("int loop 1\n")
remote_connection.send("ip address 2.2.2.2 255.255.255.255\n")
remote_connection.send("router ospf 1\n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")

for n in range (2,21):
    print "Creating VLAN " + str(n)
    remote_connection.send("vlan " + str(n) +  "\n")
    remote_connection.send("name Python_VLAN " + str(n) +  "\n")
    time.sleep(0.5) # add .5 sec to the loop when creating vlans

remote_connection.send("end\n")

time.sleep(1) #sleep 1 second before outputting the session
output = remote_connection.recv(65535)
print output

ssh_client.close


"""
NOTES FOR CONFIGURING SWITCH WITH SSH

S1>en
S1#conf t
Enter configuration commands, one per line. End with CNTL/Z.
S1(config)#host S1
S1(config)#ip domain
S1(config)#ip domain-n
S1(config)#ip domain-name DOMAIN.com
S1(config)#cry
S1(config)#crypto key
S1(config)#crypto key ge
S1(config)#crypto key generate rsa

How many bits in the modulus [512]: 1024


S1(config)#enab
S1(config)#enable pas
S1(config)#enable password cisco
S1(config)#usern
S1(config)#username elvin pas
S1(config)#username elvin password cisco
S1(config)#user
S1(config)#userna
S1(config)#username elvin pri
S1(config)#username privelege 15
S1(config)#line vty 0 4
S1(config-line)#login local
S1(config-line)#tr
S1(config-line)#transport in
S1(config-line)#transport input all
S1(config-line)#end
S1#

"""