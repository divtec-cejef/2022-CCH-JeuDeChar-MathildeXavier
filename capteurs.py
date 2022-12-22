#Gestion des différents boutons disponible sur le robot
import main
#permet de faire fonctionner plusieurs def en meme temps
from threading import Thread
BP = main.BP

BT_URGENCE = BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)

def bt_urgence (self):
    try:
         value = 0
         while not value:




