 #####                                    ######
#     # #####   ####  #    # ##### #    # #     # #
#       #    # #    # #    #   #   #    # #     # #
#  #### #    # #    # #    #   #   ###### ######  #
#     # #####  #    # # ## #   #   #    # #       #
#     # #   #  #    # ##  ##   #   #    # #       #
 #####  #    #  ####  #    #   #   #    # #       #

import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 44
instance = dht11.DHT11(pin=4)

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("Last valid input: " + str(datetime.datetime.now()))
		#temp = result.temperature()
		print("Temperature: %-3.1f C" % result.temperature)
                print("Humidity: %-3.1f %%" % result.humidity)
		if result.temperature > 18.4:
			GPIO.setup(24, GPIO.OUT)
			GPIO.output(24, True)
			GPIO.setup(26, GPIO.OUT)
                        GPIO.output(26, False)
			print("Green Light")
		else:
			GPIO.setup(26, GPIO.OUT)
                        GPIO.output(26, True)
			GPIO.setup(24, GPIO.OUT)
                        GPIO.output(24, False)
                        print("Red Lights")
	    time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
