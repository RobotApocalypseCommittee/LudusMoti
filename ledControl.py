#Import module
import RPi.GPIO as GPIO

class LedDriver:
    def __init__(self):
        #set the board mode as standard (just ignore this)
        GPIO.setmode(GPIO.BCM)

        chanList = [21, 26]

        #setup all the pins in the array as output pins
        GPIO.setup(chanList, GPIO.OUT)

        self.leds = {
            21: False,
            26: False
        }

    def set_led(self, ledno, state):
        self.leds[ledno] = state
        GPIO.output(ledno, state)

    def toggle_led(self, ledno):
        state = self.leds[ledno] = not self.leds[ledno]
        GPIO.output(ledno, state)
