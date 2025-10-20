import time
import board
import busio

# The following sensor driver is incorrect. 
from ltr381rgb import LTR_381RGB

i2c1 = busio.I2C(scl=board.GP15, sda=board.GP14)


# optical sensor
optical = LTR381RGB(i2c1)
optical.model = "CS"
optical.enable()


# als and raw data plotter
while True:
    print(f"ALS: {optical.lux} lx")
    print(optical.raw_data)
    time.sleep(0.5)