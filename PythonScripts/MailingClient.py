"""

Created by: Elvin Rivera
10/28/2020

Description: script to login to existing mail account, use SMTP protocol with script,
in order to send mail from that account to others.

TLDR: sends email using python

"""

#Importing the necessary libraries
import smtplib #used to send mail
from email import encoders 
from email.mime.text import MIMEText # ordinary text that we use
from email.mime.base import MIMEBase # use for attachment
from email.mime.miltipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25) #google your SMTP Server (yahoo, etc.)

server.ehlo() #function to call the service

# server.login('mail@mail.com', 'password123') #dont save password in plain text, encrypted text file and import then decrypt


# 'r' is read mode
with open('password.txt', 'r') as f:
    password = f.read()


server.login('mailtesting@gmail.com', password)

# create the message using the libraries above

msg = MIMEMultipart() # define the header
msg['From'] = 'Elvin'
msg['To'] = 'targetmail@gmail.com'
msg['Subject'] = 'Just a Test'

#create a txt file to import and use (contains the body of your email)
with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

# next attach an image (for this example, image needs to be in same directory as this script and the message.txt)
filename = 'coding.jpg'
attachment = open(filename, 'rb') #rb is read byte

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p) #encode the image data we just read and set as payload
p.add_header('Content-Dispoistion', f'attachment; filename={filename}') # add header to p
msg.attach(p)

text = msg.as_string() #get the whole thing as string and can be sent by server
server.sendmail('mailtesting@gmail.com', 'targetemail@gmail.com', text)
