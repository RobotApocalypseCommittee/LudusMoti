import serial
import time

class Neopixel:
    def __init__(self, port_name, num_pixels):
        self.ser = serial.Serial(port_name)
        self.num_pixels = num_pixels
        self.clear()

    def toggle_led(self):
        self.ser.write(bytes([1]))       

    def _setpixel(self, pos, r, g, b):
        self.ser.write(bytes([2,pos,r,g,b]))

    def set_pixel(self, pos, r, g, b):
        if pos < self.num_pixels and not (r > 255 or g > 255 or b > 255):
            # Valid call
            self._setpixel(pos, r, g, b)
        else:
            print("Bad Request")
    def set_all(self, r, g, b):
        for i in range(self.num_pixels):
            self.set_pixel(i, r, g, b)
    def clear(self):
        self.set_all(0,0,0)

    def _wheelpos(self, wheelpos):
        """Slightly stolen from strandtest."""
        wheelpos = 255-wheelpos
        if(wheelpos < 85):
            return (255 - wheelpos * 3, 0, wheelpos * 3)
        if(wheelpos < 170):
            wheelpos -= 85
            return (0, wheelpos * 3, 255 - wheelpos * 3)
        wheelpos -= 170
        return (wheelpos * 3, 255 - wheelpos * 3, 0)
    
    def rainbow(self):
        for j in range(256):
            for i in range(self.num_pixels):
                x = self._wheelpos((i+j) & 255)
                self.set_pixel(i,x[0],x[1],x[2])
            time.sleep(0.02)
    
    def close(self):
        self.ser.close()