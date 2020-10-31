"""

Created by: Elvin Rivera
date: 10/30/2020

Description: Server portion of the Chat room. Broadcast message from client, handle client connections.
Visual shows client connected with the (address, client), and shows the nickname of that client


E.g. Output

Connected with ('127.0.0.1', 64201)
Nickname of the client is Geek!
Connected with ('127.0.0.1', 64203)
Nickename of the client is Nerd!
"""


import threading
import socket

host = '127.0.0.1'  # Using local host
port = 55555     # don't choose a reserved port

# start the service
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) # bind to the tuple
server.listen() #puts server into listening mode for new connections

# create list for clients and nicknames, for new connections
clients = []
nicknames =[]

#functions

#sends message to all clients connected to the server
#broadcast message to all the clients in the server
def broadcast(message):
    for client in clients:
        client.send(message)

# handle the client connections
# receive messages clients and then send to other clients
def handle(client):
    while True: #endless loop
        try:  #try to receive message from client, if it succeeds, broadcast message to all clients including this one
            message = client.recv(1024) #bytes
            broadcast(message)
        except: #if it fails remove client from the list and terminate this function/loop
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index] #clients will have the same index for clients and nicknames
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break


# combines everything into one function
def receive():
    while True:
        client, address = server.accept() #accepts all the connections
        print(f"connected with {str(address)}") #returns client and address of the clients, print on the server console not broadcast

        #asking the client for the nickname, not visible to the user of the client
        #sends nickname to the server so it knows who you are
        client.send('NICK'.encode('ascii')) #KEYWORD for server (nickname)
        nickname = client.recv(1024).decode('ascii') #recieve nickname from client
        nicknames.append(nickname) #append nickname to list
        clients.append(client) #append client to list

        #formatted string print(f'SAMPLE {important_val} SAMPLE TXT')
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii')) #everyone knows the nickname of client
        client.send('Connected to the server!'.encode('ascii')) #send message to the client who just connected, indicates they can start chatting

        # method for handling threads (process messages at the same time, not serially)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start() #python threads use start method not run method

print("Server is listening...")
receive() #medhod to call it
