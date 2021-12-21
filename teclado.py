#ESTE CODIGO ES INUTIL DADO QUE EXISTE UN BOTON EN MINECRAFT QUE AUTOMATICAMENTE HACE ESTO

import keyboard
import mouse
from time import sleep
while(True):
    if(keyboard.is_pressed('b')):
        keyboard.send("t")
        sleep(0.5)
        keyboard.write("/gamemode survival imulli")
        keyboard.send("enter")
            
    elif(keyboard.is_pressed('v')):
        keyboard.send("t")
        sleep(0.5)
        keyboard.write("/gamemode survival imulli")
        keyboard.send("enter")

