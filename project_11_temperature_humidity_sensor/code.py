import time
import board
import busio
from adafruit_sht31d import SHT31D

i2c1 = busio.I2C(scl=board.GP15, sda=board.GP14)

# temperature and humidity sensor
sht_sensor = SHT31D(i2c1)

loopcount = 0
while True:
    print(f"\nTemperature: %0.1f C" % sht_sensor.temperature)
    print("Humidity: %0.1f %%" % sht_sensor.relative_humidity)
    loopcount += 1
    time.sleep(1)

    if loopcount == 10:
        loopcount = 0
        sht_sensor.heater = True
        print("Sensor Heater status =", sht_sensor.heater)
        time.sleep(1)
        sht_sensor.heater = False
        print("Sensor Heater status =", sht_sensor.heater)
