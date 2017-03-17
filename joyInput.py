"""Module for managing Joystick inputs"""

import pygame
import utils

#Various buttons and corresponding values
button_map = {
    "ledall": 0,
    "ledleft": 4,
    "ledright": 5
}

class Joystick:
    """Wrapper around pygame joystick"""
    def __init__(self, joystick_no=0):
        self.joystick_no = min(joystick_no, pygame.joystick.get_count())

        self.joystick = pygame.joystick.Joystick(self.joystick_no)
        self.joystick.init()

        self.state = {}

    def get_joy_value(self, i, invert):
        """Get absolute values from the joystick, inverting if needed"""
        val = self.joystick.get_axis(i)
        if invert:
            return val * -1
        else:
            return val

    def get_motor_vals(self):
        """Convert absolute values into values for the motors using Utils"""

        x = self.get_joy_value(0, 0)
        y = self.get_joy_value(1, 1)

        val = utils.convertToMotorSpeed(x, y)
        return val

    def get_button(self, n):
        """Returns button value"""

        return self.joystick.get_button(n)

    def update(self):
        """Updates the Joystick every frame with any changes"""
        state = {}
        for key in button_map:
            state[key] = self.get_button(button_map[key])
        state["motor_vals"] = self.get_motor_vals()
