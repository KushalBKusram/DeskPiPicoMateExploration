import board
import digitalio

# PIR Sensor
pir_sensor = digitalio.DigitalInOut(board.GP28)
pir_sensor.direction = digitalio.Direction.INPUT
pir_sensor.pull = digitalio.Pull.DOWN

last_value = pir_sensor.value

while True:
    if last_value != pir_sensor.value:
        last_value = pir_sensor.value
        print('Motion ' + ('detected!' if pir_sensor.value else 'stopped'))