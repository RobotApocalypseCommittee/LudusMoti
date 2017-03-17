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

        #set default states as off
        self.off()

    def set_led(self, state):
        """Manually change led states"""
        self.state = state
        self.update()

    def toggle_led(self):
        """Toggle Leds"""
        self.state = not self.state
        self.update()

    def blink(self):
        """Blink function; needs to implemented in main"""
        self.blinking = True

    def off(self):
        """Set all states to 0"""
        self.state = False
        self.blinking = False
        self.blink_count = 0
        self.update()

    def update(self):
        """Updates LED state."""

        if self.blinking:
            self.blink_count += 1

        if self.blink_count == 100:
            self.state = not self.state
            self.blink_count = 0

        GPIO.output(self.pinNo, self.state)

    