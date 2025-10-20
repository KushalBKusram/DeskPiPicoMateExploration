import time
import board
import busio
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

i2c1 = busio.I2C(board.GP15, board.GP14)

# 6-axis IMU Sensor
imu_sensor = LSM6DS3TRC(i2c1)

# Acceleration plotter
while True:
    print(imu_sensor.acceleration)
    time.sleep(0.1)

# Gyro plotter
while True:
    print(imu_sensor.gyro)
    time.sleep(0.1)