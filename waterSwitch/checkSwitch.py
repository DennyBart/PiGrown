import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous = "null"

while True:
    state = GPIO.input(26)
    if state == False and previous == "open" or state == False and previous == "null":
        print('Circuit Closed.')
        previous = "closed"
    if state != False and previous == "closed" or state != False and previous == "null":
        print('Circuit Open.')
        previous = "open"
    sleep(1)

GPIO.cleanup(26)
