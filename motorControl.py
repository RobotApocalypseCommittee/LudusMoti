from rrb3 import *

#Class for functions on the motorshield using RRB3

class MotorController:
    def __init__(self, involts=9, motorvolts=6):
        """Initialse with default voltages"""
        self.rrb = RRB3(involts, motorvolts)
        self.motors = [(0,0), (0,0)]

    def set_led(self, led_no=0, state=False):
        """Method for controlling Leds"""
        if led_no==0:
            self.rrb.set_led1(state)
        else:
            self.rrb.set_led2(state)

    def motor_update(self):
        """Update Motors!"""
        self.rrb.set_motors(self.motors[0][1], self.motors[0][0], self.motors[1][1], self.motors[1][0])

    def set_motor(self, motor_no, direction, speed):
        """Assigning values for updating motors"""
        if motor_no in [0,1]:
            self.motors[motor_no] = (direction, speed)
        self.motor_update()