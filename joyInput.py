import pygame
import utils

button_map = {
    "ledall": 0,
    "ledleft": 4,
    "ledright": 5
}

class Joystick:

    def __init__(joystick_no=0):
        self.joystick_no = min(joystick_no, pygame.joystick.get_count())

        self.joystick = pygame.joystick.Joystick(self.joystick_no)
        self.joystick.init()

        self.state = {}

    def getJoyValue(self, i, invert):
        val = self.joystick.get_axis(i)
        if invert:
            return val * -1
        else:
            return val


    def get_motor_vals(self):

        x = self.getJoyValue(0, 0)
        y = self.getJoyValue(1, 1)

        val = utils.convertToMotorSpeed(x, y)
        return val

    def get_button(self, n):

        return self.joystick.get_button(n)

    def update(self):
        state = {}
        for key in button_map.keys():
            state[key] = self.get_button(button_map[key])
        state["motor_vals"] = self.get_motor_vals()
