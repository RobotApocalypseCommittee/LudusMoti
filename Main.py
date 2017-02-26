import pygame

pygame.init()

done = False

clock = pygame.time.Clock()

pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

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
    if y > 0:
        
        if x > 0:
            a = y
            b = y + x
            
        elif x < 0:
            a = y + x
            b = y
            
        else:
            a = y
            b = y
            
    elif y < 0:
        
        if x > 0:
            a = y
            b = y - x
            
        elif x < 0:
            a = y - x
            b = y
            
        else:
            a = y
            b = y
            
    elif y == 0:
        a = 0
        b = 0

    a = mapToValue(round(a, 2), -2, 2, -1, 1)
    b = mapToValue(round(b, 2), -2, 2, -1, 1)

    return a, b
        

for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

 
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

            print val
            
            '''
            counter = 0
            for i in range(2):
               print getJoyValue(i, counter)
               counter += 1
            '''
        clock.tick(20)
        
    except KeyboardInterrupt:
        pygame.quit()
        break

pygame.quit()
