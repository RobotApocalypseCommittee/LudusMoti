#Miscellaneous functions go here

def mapToValue(x, a, b, i, j):
    # Here's a function that takes in the value x, which is between a and b,
    # and is to be mapped to a value between i and j.

    if b != a and i != j:
        return x/float(b-a)*float(j-i)

#Function to convert absolute values into speeds for the motors
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
