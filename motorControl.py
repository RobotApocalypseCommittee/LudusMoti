from rrb3 import *

#Class for functions on the motorshield using RRB3

class MotorController:
    #Initialse with default voltages
    def __init__(self, involts=9, motorvolts=6):
        self.rrb = RRB3(involts, motorvolts)
        self.motors = [(0,0), (0,0)]

    #Method for controlling leds
    def set_led(self, led_no=0, state=False):
        if led_no==0:
            self.rrb.set_led1(state)
        else:
            self.rrb.set_led2(state)

    #Update motors
    def motor_update(self):
        self.rrb.set_motors(self.motors[0][1], self.motors[0][0], self.motors[1][1], self.motors[1][0])

    #Assign values to update motors
    def set_motor(self, motor_no, direction, speed):
        if motor_no in [0,1]:
            self.motors[motor_no] = (direction, speed)
        self.motor_update()