import time
import board
import busio
from adafruit_mmc56x3 import MMC5603


i2c1 = busio.I2C(scl=board.GP15, sda=board.GP14)

# MMC5603 magentometer
magnetometer = MMC5603(i2c1)
magnetometer.data_rate = 1000 # in Hz, from 1-255 or 1000
magnetometer.continuous_mode = True


# Magnetic plotter
while True:
    print(magnetometer.magnetic)
    time.sleep(0.1)