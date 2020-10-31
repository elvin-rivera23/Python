"""

Created by: Elvin Rivera
date: 10/30/2020

Description: Client portion of Chatroom. Allows client to connect, NICK is passed to server.
Visual shows nickname of someone who connects and messages


E.g. Output

--client1
Choose a nickname: Geek
Geek joined the chat!
Connected to the server!
Nerd joined the chat!
Hey everybody!
Geek: Hey everybody

--client2
Choose a nickname: Nerd
Nerd joined the chat!
Connected to the server!
Geek: Hey everybody
"""

import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK': #receive KEYWORD
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error has occurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

#write a receive thread
receive_thread = threading.Thread(target=receive) # target function
receive_thread.start()

#write a write thread
write_thread = threading.Thread(target=write) #target function
write_thread.start()
