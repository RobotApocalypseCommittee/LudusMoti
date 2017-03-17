##### Code to drive the Pibot #####

#Various modules to be imported
import pygame
import motorControl
import RPi.GPIO as GPIO
import joyInput
import ledControl

#Start Pygame  
pygame.init()

#loop not finished
done = False

#Initialise frames per second
clock = pygame.time.Clock()

#Start Pygame's joysticks
pygame.joystick.init()

#Initalise a motor control object
motorControl = motorControl.MotorController()

#Initalise a new joystick
joystick = joyInput.Joystick()

#Pin numbers for leds
ledChannels = [21, 26]

#Initalise led object for all of them
leds = [ledControl.Led(i) for i in ledChannels]


### The Main Loop ###

while not done:
    try:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

        #Get new values from joystick
        joystick_data = joystick.update()

        #Assign them to generic variables
        val = joystick_data["motor_vals"]

        ledleft = joystick_data["ledleft"]
        ledright = joystick_data["ledright"]

        ledall = joystick_data["ledall"]
        
        if ledall:
            ledleft = 1
            ledright = 1

        #Set leds on the motorshield
        motorControl.set_led(0, ledleft)
        motorControl.set_led(1, ledright)

        print (ledleft)

        #Set pinout leds
        leds[0].set_led(ledleft)

        leds[1].set_led(ledright)


        ## Drive the motors
        for i in range(2):
            motorControl.set_motor(i, val[2], val[i])

        #Frames per second
        clock.tick(100)

    #Detect for Ctrl+C on Pi to break Pygame loop
    except KeyboardInterrupt:
        pygame.quit()
        break

#Clean pins and close pygame
GPIO.cleanup()
pygame.quit()
