
import pywhatkit as kit

import datetime

x = datetime.datetime.now()
print(x)

try :              #Sendnum                 #Text                                              #SendTime
    kit.sendwhatmsg ("+90xxxxxxxxxx","Hi, I'm Suleyman , This message send by python. Thanks", 15,38)
    print("your message has been sent successfully.")
except :
    print("unexpected error.")
