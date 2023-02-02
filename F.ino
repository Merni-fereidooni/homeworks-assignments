#include <Adafruit_GFX.h> // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library
#include <SPI.h>

#define CS 10 // Chip select pin for LCD
#define DC 9 // Data/command pin for LCD
#define RST 8 // Reset pin for LCD

//Create two LCD screens
Adafruit_ST7735 tft1 = Adafruit_ST7735(CS, DC, RST);
Adafruit_ST7735 tft2 = Adafruit_ST7735(CS, DC, RST);

//Load image
#include "image.h"

void setup(){
  // Initialize both screens
  tft1.initR(INITR_BLACKTAB);
  tft2.initR(INITR_BLACKTAB);

  //Set rotation for both screens
  tft1.setRotation(3);
  tft2.setRotation(1);

  //Draw image to both screens
  tft1.drawBitmap(0, 0, image_reverse, 128, 128, ST7735_BLACK);
  tft2.drawBitmap(0, 0, image, 128, 128, ST7735_BLACK);

}

void loop(){
 //Nothing to do here
}
