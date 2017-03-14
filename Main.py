import pygame
import motorControl
import RPi.GPIO as GPIO
import joyInput
import ledControl

pygame.init()

done = False

clock = pygame.time.Clock()

pygame.joystick.init()

motorControl = motorControl.MotorController()

joystick = joyInput.Joystick()

leds = ledControl.LedDriver()

leftState = 0

while done == False:
    try:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop


        joystick_data = joystick.update()


        val = joystick_data["motor_vals"]

        ledleft = joystick_data["ledleft"]
        ledright = joystick_data["ledright"]

        ledall = joystick_data["ledall"]

        if ledall:
            ledleft = 1
            ledright = 1

        motorControl.set_led(0, ledleft)
        motorControl.set_led(1, ledright)

        print ledleft
        leds.set_led(21, ledleft)

        leds.set_led(26, ledright)

        #GPIO.output(14, ledright)


        for i in range(2):
            motorControl.set_motor(i, val[2], val[i])


        clock.tick(100)

    except KeyboardInterrupt:
        pygame.quit()
        break

GPIO.cleanup()
pygame.quit()
