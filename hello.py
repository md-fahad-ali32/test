import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Back, Style
import requests as req
if os.system('pip install colorama requests'):
   os.system("clear")
else:
   os.system("clear")

text = '''
 ▄▄▄▄    ▒█████   ▄▄▄▄    ███▄ ▄███▓▓█████ ▒██   ██▒
▓█████▄ ▒██▒  ██▒▓█████▄ ▓██▒▀█▀ ██▒▓█   ▀ ▒▒ █ █ ▒░
▒██▒ ▄██▒██░  ██▒▒██▒ ▄██▓██    ▓██░▒███   ░░  █   ░
▒██░█▀  ▒██   ██░▒██░█▀  ▒██    ▒██ ▒▓█  ▄  ░ █ █ ▒
░▓█  ▀█▓░ ████▓▒░░▓█  ▀█▓▒██▒   ░██▒░▒████▒▒██▒ ▒██▒
░▒▓███▀▒░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░   ░  ░░░ ▒░ ░▒▒ ░ ░▓ ░
▒░▒   ░   ░ ▒ ▒░ ▒░▒   ░ ░  ░      ░ ░ ░  ░░░   ░▒ ░
 ░    ░ ░ ░ ░ ▒   ░    ░ ░      ░      ░    ░    ░
 ░          ░ ░   ░             ░      ░  ░ ░    ░
      ░                ░
'''
print(Fore.BLUE + text)
print(Style.RESET_ALL)
print('   1.Deafult')
print('   2.Custom')
print('   3.Update')
result = str(input('Select=> '))
if result == '1':
    print('ok')
    sender_email = "alivoipai@gmail.com"
    receiver_email = str(input('Receiver Mail Adress=>'))
    password = "@@1234@@"
    message = MIMEMultipart("alternative")
    message["Subject"] = str(input('Subject=>'))
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = str(input('Msg=>'))
    rng = input('Rnage=>')
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "html")

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    for i in range(int(rng)):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print('Sent email '+str(i+1))

elif result == '3':
    pass
