import socket
import threading

from queue import Queue

target = '127.0.0.1' #choose the IP to DDoS, or a domain name (used local machine, default gateway IPConfig)
queue = Queue()
open_ports = [] # list to add all the open ports at the end

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create internet socket, TCP
        sock.connect((target, port)) #connect, requires a tuple
        return True
    except:
        return False

# print(portscan(80)) #to test the portscan function

"""
# long way of checking every port
for port in range(1, 1024):
    result = portscan(port)
    if result:
        print("Port {} is open!".format(port))
    else:
        print("Port {} is closed!".format(port))

"""


# for ports in the port list, we are going to put every port to the list queue
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

# function that threads are using, every thread executes
# as long as queue isn't empty get next port, if portscan is true, print that it's open and add to port list
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = [] # define empty thread list

for t in range(100):
    thread = threading.Thread(target=worker) # not calling worker function, just referring to it
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list: 
    thread.join() # wait for thread to finish

print("Open ports are: ", open_ports) # dont want this to print until all the threads are done

