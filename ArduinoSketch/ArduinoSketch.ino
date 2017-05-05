#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

//Parameters neopixel strip(tested with a single neopixel).
#define PIN            6
#define NUMPIXELS      1

bool led = false;

// The neopixel object.
Adafruit_NeoPixel strip;
//Various bytes that will be recieved...
byte brightness;
byte target;
byte red, green, blue;



void setup() {
  // Setup debug led.
  pinMode(13, OUTPUT);

  // Setup strip(make sure to get          V THIS BIT V correct.
  strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_RGB + NEO_KHZ800);
  strip.begin();

  // Begin Serial
  Serial.begin(9600);
  while (!Serial);

}

void loop() {
  if (Serial.available()) {
    // read the incoming byte:
    byte chacom = Serial.read();

    // Split it into channel, and command(in case we ever need more than one strip.)
    byte channel = (chacom & B11100000) >> 5;
    byte command = chacom & B00011111;
    
    handle_command(channel, command);  
  }
}

void handle_command(byte channel, byte command) {
  switch (command) {
    case 1:
      // Toggle LED
      led = !led;
      digitalWrite(13, led);
      break;
    case 2:
      // Set colour of pixel.
      target = waitForByte();
      
      red = waitForByte();
      green = waitForByte();
      blue = waitForByte();
      
      strip.setPixelColor(target, red,green,blue);
      strip.show();
      break;
    case 3:
      // Set brightness of strip.
      brightness = waitForByte();
      
      strip.setBrightness(brightness);
      strip.show();
      break;
  }
}

byte waitForByte() {
  while (!Serial.available());
  return Serial.read();
}

