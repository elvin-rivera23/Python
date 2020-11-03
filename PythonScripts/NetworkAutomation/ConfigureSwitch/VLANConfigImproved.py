"""

Created by: Elvin Rivera
Date: 11/3/2020

Description: 

~ This is continuing the script, dont' need to embed username and password. 
    - You will be prompted to enter that instead
~ This also creates a loop for creating VLAN's
    - don't need to copy and paste the vlan config portion


NOTE: using GNS3
"""

#!/usr/bin/env python   <---unix #! , executable file that's meant to be interpreted can choose interpretor

import getpass
import sys
import telnetlib

HOST = "192.168.122.72"
user = raw_input("Enter your telnet username: ")    #this is what changed from original script raw_input vs input
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")


tn.write("conf t\n")

"""

Remove:

tn.write("enable\n")
tn.write("cisco\n")


# on switch, change vty line to provide privileges when we login

S1#sh run | i user
username Elvin password 0 cisco
S1#conf t
S1(config)#user Elvin pr
S1(config)#user Elvin privelege 15
S1(config)#end

S1#sh ip in
S1#telnet 192.168.122.72

# Next time you login you will be in privliged mode
# won't need option enable
"""

# --- LOOP PORTION OF CODE FOR CREATING VLAN ---

"""

# create a loop that writes to the switch

tn.write("vlan " + n + "\n")
tn.write("name Python_VLAN_2\n")

"""
# creates VLAN 2-100, add 1 extra value for range
for n in range (2,101):
    tn.write("vlan " + str(n) + "\n")   #n is an integer and needs to be converted to string
    tn.write("name Python_VLAN_" + str(n) + "\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
