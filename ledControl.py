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

        self.blink_delay = 100
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

    def blink(self,bd=100):
        """Blink function; needs to implemented in main"""
        self.blinking = True
        self.blink_delay = bd
        self.update()

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

        if self.blink_count == self.blink_delay:
            self.state = not self.state
            self.blink_count = 0

        GPIO.output(self.pinNo, self.state)

class LEDriver:
    def __init__(self):
        #Pin numbers for leds
        #led_channels are [21, 26]
        self.blinkyTimes = False
        self.leo = Led(21)
        self.rob = Led(26)
        #Initalise led object for all of them
        self.leds = [self.leo, self.rob]

    def update(self, joystick_data):
        """Updates the leds"""
        for event in joystick_data["events"]:
            if event[0] == "ledblinkon":
                self.blinkyTimes = not self.blinkyTimes
                for led in self.leds:
                    if self.blinkyTimes:
                        led.blink()
                    else:
                        led.off()
            elif event[0] == "ledblinkspdup":
                for led in self.leds:
                    led.blink_delay += 10
            elif event[0] == "ledblinkspddown":
                for led in self.leds:
                    led.blink_delay -= 10
        for led in self.leds:
            led.update()
