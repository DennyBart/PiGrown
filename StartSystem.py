import RPi.GPIO as GPIO
import time
from time import sleep
import schedule
import datetime
GPIO.setmode(GPIO.BCM)
#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

email_sent = False #Bool to send mail if water tank low
previous = "null"
soillimit = 20 #Place Holder for defined soil moisture limit

def get_last_watered():
    with open('watered.txt') as lasttime:
        lastline=(list(lasttime)[-1]) #Get last line of file        
        return find_day_month(lastline)
        print (lastline)

def find_day_month(date): #Returns the day and month as INT
    month = (date[5:7])
    day = (date[8:10])
    return (month, day)

def get_status(pin): #Returns the status of a pin
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def init_output(pin): #Initialise pin by providing pin NO 
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def waterlevel(water_pin=26): #Check Water Level Circuit
    init_output(water_pin)
    #Check circuit on pin and casts INT to BOOL (Low is True - High is False)
    return bool(GPIO.input(26))

def soilsens(moisture): #Place holder for soil sensor
    if moisture < soillimit:
        startpump()
    else:
        print('All OK with Soil')


def startpump(pump_pin = 4, delay = 1): #Start pump
    f = open("watered.txt", "a") # Write to file to store last ran date
    currenttime = str(datetime.datetime.now())
    f.write("{}\n".format(datetime.datetime.now()))
    f.close()
    init_output(pump_pin)
    GPIO.output(pump_pin, GPIO.HIGH) #PumpOff
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.LOW) #PumpON
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH) #PumpOff


def pumpcheck(): #Check the last time the pump was ran
   currentdate = str(datetime.datetime.now())
   last_water = get_last_watered()
   today = find_day_month(currentdate)
   if last_water[1] != today[1]:
       print("Watering!")
       startpump()
       email_sent = False #Reset email bool so that a email can be sent once watered again and water lever low
   else:
       print ('Already watered today')



#Schedule Events
schedule.every(5).seconds.do(pumpcheck)

while True:
    schedule.run_pending()
    if waterlevel() == False and email_sent == False:
        print("Call EMAIL Class")
        email_sent = True
    time.sleep(3)




#GPIO.cleanup(26)
