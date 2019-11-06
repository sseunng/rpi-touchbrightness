import time
from datetime import datetime
import threading
from rpi_backlight import Backlight

backlight = Backlight()

# Default brightness
high = 80
low = 30

def onTouch():
    while True :
        file = open( "/dev/input/mice", "rb" )
        buf = file.read(3)
        if (buf is not None) :
            file.close()
            backlight.brightness = high
            time.sleep(10)
            with backlight.fade(duration=1) :
                backlight.brightness = low


def onTime():
    global high, low
    while True :
        now = datetime.now()
        hour = now.hour

        if (hour >= 0 and hour <= 5) :
            high = 20
            low = 5
        elif (hour >= 6 and hour <= 8) :
            high = 40
            low = 10
        elif (hour >= 9 and hour <= 16) :
            high = 80
            low = 30
        elif (hour >= 17 and hour <= 22) :
            high = 50
            low = 20
        elif (hour == 23) :
            high = 30
            low = 10

        with backlight.fade(duration=1) :
            backlight.brightness = low

        time.sleep(60)


t1 = threading.Thread(target=onTouch)
t2 = threading.Thread(target=onTime)

t1.start()
t2.start()
