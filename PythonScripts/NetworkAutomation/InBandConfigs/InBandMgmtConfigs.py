"""

Created by: Elvin Rivera
Date: 11/9/2020

Description: Saving Configs with an In-Band Network



NOTE: using GNS3, refer to InBandNetwork.png
"""

#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

# NOTE: If spanning tree is converging, or problem on the network, script will not have access to network devices
# out-of-band typically better than in-band
for n in range (72,77):
    print "Telnet to host" + str(n)
    HOST = "192.168.122." + str(n)
    tn = telnetlib.Telnet(HOST)

 tn.read_until("Username: ")
 tn.write(user + "\n")

 if password:
     tn.read_until("Password: ")
     tn.write(password + "\n")

 tn.write("conf t\n")

 for n in range (2,21):
     tn.write("vlan " + str(n) + "\n")
     tn.write("name Python_VLAN_" + str(n) + "\n")

 tn.write("end\n")
 tn.write("wr\n") # code to save configuration of devices
 tn.write("exit\n")
 print tn.read_all()