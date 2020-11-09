"""

Created by: Elvin Rivera
Date: 11/9/2020

Description: Backup Configurations


NOTE: using GNS3, refer to BackupConfigTopology.png
"""

#!/usr/bin/env python

import getpass
#import sys
import telnetlib

# Get Username and Password
user = raw_input("Enter your username: ")
password = getpass.getpass()

#  Open file with list of switches
f = open ("myswitches")

#  Telnet to each switch and cofigure it
for line in f:
	print "Getting running-config " + (line) #print IP of switch
	HOST = line.strip() #strips whitespace
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n") #write username from the "user" in the above code
	if password:
	    tn.read_until("Password: ")
	    tn.write(password + "\n")

	tn.write("terminal length 0\n") #shows full config on switch, dont press space on the switch
	tn.write("show run\n")
	tn.write("exit\n")

        readoutput = tn.read_all()  #tn is the the variable we are using for the session in the for loop
        saveoutput =  open("switch" + HOST, "w") #saving to a file "w" = write
        saveoutput.write(readoutput)
        saveoutput.write("\n")
	    saveoutput.close
        print tn.read_all()