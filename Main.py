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

ledDriver = ledControl.LEDriver()

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

        ledDriver.update(joystick_data)
        

        ## Drive the motors
        for i in range(2):
            motorControl.set_motor(i, val[2], val[i])

        # Frames per second(more realistic)
        clock.tick(50)

    #Detect for Ctrl+C on Pi to break Pygame loop
    except KeyboardInterrupt:
        pygame.quit()
        break

#Clean pins and close pygame
GPIO.cleanup()
pygame.quit()
