#Import module
import RPi.GPIO as GPIO

#set the board mode as standard (just ignore this)
GPIO.setmode(GPIO.BCM)

#Individual leds become new class instances
class Led:
    def __init__(self, pin):

        self.pinNo = pin
        
        #setup led as output
        GPIO.setup(self.pinNo, GPIO.OUT)
        
        #set default state as off
        self.state = False

        self.blinking = False

        self.happy = True
        

    def set_led(self, state):
        self.state = state
        GPIO.output(self.pinNo, state)

    def toggle_led(self):
        state = not self.state
        GPIO.output(ledno, state)

    def blink(self):
        if blinking:
            self.toggle_led()
        else:
            self.blinking = True

    def kill(self):
        self.state = False
        self.blinking = False

    
    