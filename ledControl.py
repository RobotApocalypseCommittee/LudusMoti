#Import module
import RPi.GPIO as GPIO

#set the board mode as standard (just ignore this)
GPIO.setmode(GPIO.BCM)

chanList = [21, 26]

#setup all the pins in the array as output pins
GPIO.setup(chanList, GPIO.OUT)

ledleft = True
ledright = False

#Output to (pin, state)
GPIO.output(21, ledleft)

GPIO.output(26, ledright)

#Reset all the pins after use
GPIO.cleanup()
