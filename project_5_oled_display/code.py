import time
import board
import busio
from adafruit_ssd1306 import SSD1306_I2C

i2c0 = busio.I2C(scl = board.GP17, sda = board.GP16)


# 0.96" 128x64 OLED Display
display = SSD1306_I2C(128, 64, i2c0)

def display_text(str, line):
   display.text(str, 0, (line % 8) * 8, 1, font_name="/lib/font5x8.bin") 

while True:
   display.fill(0)

   display_text("Hello!", 0)
   # Programmed on the day of Diwali
   display_text("Happy Diwali!", 2)

   display.show()

   time.sleep(0.5)