import pygame
import motorControl
import RPi.GPIO as GPIO

pygame.init()

done = False

clock = pygame.time.Clock()

pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

motorControl = motorControl.MotorController()

GPIO.setmode(GPIO.BCM)

chanList = [21, 26]

GPIO.setup(chanList, GPIO.OUT)

def getJoyValue(i, invert):
    val = joystick.get_axis(i)
    if invert:
        return val * -1
    else:
        return val

def mapToValue(x, a, b, i, j):
    # Here's a function that takes in the value x, which is between a and b,
    # and is to be mapped to a value between i and j.
    
    if b != a and i != j:
	    return x/float(b-a)*float(j-i)
	    
def convertToMotorSpeed(x, y):
    if y < 0:
        d = 0
    elif y >= 0:
        d = 1
        
    if y > 0:

        if x > 0:
            a = y
            b = y+x

        elif x < 0:
            a = y+x*-1
            b = y

        else:
            a = y
            b = y

    elif y < 0:

         if x > 0:
             a = y*-1
             b = (y-x)*-1

         elif x < 0:
             a = (y-x*-1)*-1
             b = y*-1

         else:
             a = y*-1
             b = y*-1

    elif y == 0:
        a = 0
        b = 0

    a = mapToValue(round(a, 2), -2, 2, -1, 1)
    b = mapToValue(round(b, 2), -2, 2, -1, 1)
    
    return a, b, d
        

for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

leftState = 0
 
while done == False:
    try:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop

        joystick_count = pygame.joystick.get_count()

        
        
        for i in range(1):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            x = getJoyValue(0, 0)
            y = getJoyValue(1, 1)

            val = convertToMotorSpeed(x, y)

            ledleft = joystick.get_button( 4 )
            ledright = joystick.get_button( 5 )
            
            ledall = joystick.get_button( 0 )

            if ledall:
                ledleft = 1
                ledright = 1
            
            motorControl.set_led(0, ledleft)
            motorControl.set_led(1, ledright)

            print ledleft
            GPIO.output(21, ledleft)

            GPIO.output(26, ledright)
            
            #GPIO.output(14, ledright)


            for i in range(2):
                motorControl.set_motor(i, val[2], val[i])

            
        clock.tick(100)
        
    except KeyboardInterrupt:
        pygame.quit()
        break

GPIO.cleanup()
pygame.quit()
