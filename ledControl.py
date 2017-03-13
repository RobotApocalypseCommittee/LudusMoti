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
GPIO.output(21, T)

GPIO.output(26, ledright)

def setLed(whichLed, state):
    GPIO.output(whichLed, state)
    
