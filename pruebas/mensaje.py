import pywhatkit as what
import datetime as time

num = "+XX XXXXXXXXX"
msg = "A comer"
hour = 14
minute = 15
try:
    what.sendwhatmsg(num,msg,hour,minute)
    print("Mensaje enviado")
except:
    print("El mensaje no ha llegado")