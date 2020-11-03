"""

Created by: Elvin Rivera
Date: 11/3/2020

Description: Building on the VLANConfigImproved.py

This is a script for setting up multiple Switches and Multiple VLANs


NOTE: using GNS3, refer to MultipleSwitches.PNG
"""

#!/usr/bin/env python   <---unix #! , executable file that's meant to be interpreted can choose interpretor

import getpass
import sys
import telnetlib

#same username and password for all the switches, moves to outside the loop
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

# looping through the IP of the 5 switches
for n in range (72,77):
    HOST = "192.168.122." + str(n)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")   # ask for a username but pass the variable above
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")


    tn.write("conf t\n")

    """
    eg. range(5,10)
    [5 , 6, 7, 8 , 9]
    
    will create these VLANs for all the Switches in our topology
    """
    for n in range (2,11): # subloop
        tn.write("vlan " + str(n) + "\n")   #n is an integer and needs to be converted to string
        tn.write("name Python_VLAN_" + str(n) + "\n")

    tn.write("end\n")   #goes back to privilege mode
    tn.write("exit\n")  #exit telnet session

    print tn.read_all()
    
    
    
    
"""

NOTE: in the simplest sense, shutdown turns the interface off. 
no shutdown turns the interface on (enables it). You can configure an interface in either case. 
Using the shutdown command is one of the things you can do when configuring an interface


Textpad:

enable password cisco
username Elvin privilege 15 password 0 cisco
line vty 0 4
    login local
    transport input all
    
--- Configuring Switch2

Switch>en
Switch#conf t
Enter configuration commands, one per line. End with CNTL/Z
Switch(config)#host S2
S2(config)#enable password cisco
S2(config)#username Elvin privilege 15 password 0 cisco
S2(config)#line vty 0 4
S2(config-line)#login local
S2(config-line)#transport input all
S2(config-line)#int vlan 1
S2(config-if)#no shut


S2(config-if)#ip add
S2(config-if)#ip address 192.168.122.73 255.255.255.0
S2(config-if)#end
S2#ping 192.168.122.72

S2#conf t
S2(config)#spa
S2(config)#spanning-tree vlan 1 roo
S2(config)#spanning-tree vlan 1 root ?
    primary     Configure this switch as primary root for this spanning tree
    secondary   Configure this switch as secondary root


S2(config)#spanning-tree vlan 1 root pri
S2(config)#spanning-tree vlan 1 root primary
S2(config)#end

--- NOW GO TO SWITCH 1

S1#sh ip int brief
S1#telnet 192.168.122.73
Username: Elvin
Password:
S2#exit


S1#wr


--- ON SWITCH 2

S2#wr

--- REPEAT THE PROCESS FOR SWITCH 3

Switch>en
Switch#conf t
Enter configuration commands, one per line. End with CNTL/Z
Switch(config)#host S3
S3(config)#enable password cisco
---ETC



--- ON EACH SWITCH

S2#sh vlan bri
S2#sh vlan brief

S3#sh vlan bri
S3#sh vlan brief
---ETC

"""