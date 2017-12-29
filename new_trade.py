import requests
import pickle
import os
import datetime
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

lista= []
with open('/home/mihaly/R_codes/new_crypto_trade/uj_coins.txt') as f:
    for line in f:
        lista.append(line)



# Create the base text message.
msg = EmailMessage()
me = "new_crypto_trade_opportunity@lan5025.com"
you = "ormraat.pte@gmail.com"

msg['Subject'] = "New_crypto_trade"
msg['From'] = Address("new_crypto_trade", "new_crypto_trade")
msg['To'] = Address("Orsos Mihaly", "ormraat.pte@gmail.com")

msg.set_content("This is a new crypto trade opportunity : \n"+("\n".join(lista)))
s = smtplib.SMTP('localhost')

s.send_message(msg)
s.quit()

print('email_sent')

