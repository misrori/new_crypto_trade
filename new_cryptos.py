import requests
import pickle
import os
import datetime
osszes = list(map(lambda x: x['id'], requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=0').json()))

if(os.path.exists('/home/mihaly/PYTHON/new_crypto_report/osszeslista')==False):
    pickle.dump( osszes, open( "/home/mihaly/PYTHON/new_crypto_report/osszeslista", "wb" ) )
regi = pickle.load(open( '/home/mihaly/PYTHON/new_crypto_report/osszeslista', "rb" ))
eredmeny = [item for item in osszes if item not in regi]
if len(eredmeny) ==0:
   filex = open("/home/mihaly/PYTHON/new_crypto_report/res.txt", "w")
   filex.write(str(datetime.datetime.now()))
   filex.close()

if len(eredmeny) !=0:
    import smtplib

    from email.message import EmailMessage
    from email.headerregistry import Address
    from email.utils import make_msgid

    # Create the base text message.
    msg = EmailMessage()
    me = "new_crypto@lan5025.com"
    you = "ormraat.pte@gmail.com"

    msg['Subject'] = "New crypto"
    msg['From'] = Address("new_crypto", "new_crypto")
    msg['To'] = Address("Orsos Mihaly", "ormraat.pte@gmail.com")

    msg.set_content("This is a new crypto : \n "+("\n".join(eredmeny)))
    s = smtplib.SMTP('localhost')

    s.send_message(msg)
    s.quit()
    pickle.dump( osszes, open( "/home/mihaly/PYTHON/new_crypto_report/osszeslista", "wb" ) )
    print('email_sent')
# * * * * * /home/mihaly/hadoop/anaconda3/bin/python /home/mihaly/PYTHON/new_crypto_report/new_cryptos.py >> /home/mihaly/PYTHON/new_crypto_report/res.txt
