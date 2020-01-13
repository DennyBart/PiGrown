import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous = "null"

while True:
    while not GPIO.input(26): pass
    print( "Closed Circuit" )
    while GPIO.input(26): pass
    print( "Opened Circuit" )

GPIO.cleanup(26)
