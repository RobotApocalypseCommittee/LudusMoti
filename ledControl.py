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
        self.update()

    def off(self):
        """Set all states to 0"""
        self.state = False
        self.blinking = False
        self.blink_count = 0
        self.update()

    def update(self, joystick):
        """Updates LED state."""

        if self.blinking:
            self.blink_count += 1

        if self.blink_count == 100:
            self.state = not self.state
            self.blink_count = 0

        GPIO.output(self.pinNo, self.state)

class LEDriver:
    def __init__(self):
        #Pin numbers for leds
        #led_channels are [21, 26]
        self.blinkyTimes = False
        self.blinkspd = 10
        self.leo = Led(21)
        self.rob = Led(26)
        #Initalise led object for all of them
        self.leds = [Led(i) for i in led_channels]

    def update(self, joystick_data):
        for event in joystick_data["events"]:
            if event[0] == "ledblinkon":
                self.blinkyTimes = not self.blinkyTimes
        if self.blinkyTimes:
            counter = 0
            self.leo.toggle_led
            
            


    