from socket import timeout
from pip import main
from plyer import notification
import time

def drink_water(name, message):
    notification.notify(
        title = name,
        message = message,
        app_icon = "D:\py\projects\drink_water_notify\water.ico",
        timeout = 10
    )

if __name__ == '__main__':
    while True:
        drink_water("Omkar!" , "Drink Water")
        time.sleep(1800)
        #time is in seconds 1800 seconds means 30 min

    




    