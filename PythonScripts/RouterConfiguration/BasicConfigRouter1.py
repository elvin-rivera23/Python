"""

Created by: Elvin Rivera
Date: 11/2/2020

Description: Practice using Python in a network. Creating loopback on router.

Reference: https://docs.python.org/3/library/telnetlib.html
"""

# import modules
import getpass
import sys
import telnetlib

HOST = "192.168.122.71"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

#looks for strings and sends/writes it to the router
tn.read_until("Username: ")
tn.write(user + "\n") #pass the value from User and do carriage return
if password:
    tn.read_until("Password: ") #if password is configured then look for the pw prompt
    tn.write(password + "\n")

# send commands to the router, no validation here
tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("int loop 1\n")
tn.write("ip address 2.2.2.2 255.255.255.255\n")
tn.write("router ospf 1\n")
tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()