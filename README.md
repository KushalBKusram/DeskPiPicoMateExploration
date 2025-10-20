# DeskPi PicoMate Exploration

## Getting Up and Running

I am following [DeskPi PicoMate User Manual V1.0](https://deskpi.com/blogs/learn/deskpi-picomate-user-manual-and-sources) which lists using CircuitPython 7.3.3 for this project with DeskPi PicoMate.

For the following projects, it is assumed that steps discussed in the PicoMate are completed and `CIRCUITPY` directory is successfully mounted. 

### Project 1 - Blink RGB LED

1. Create a `lib` directory on `CIRCUITPY`.
2. Copy `neopixel.py` into that directory.
3. Copy `code.py` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program. 


### Project 2 - Button

1. Copy `code.py` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program.
2. Press the button on the board and observe the result on the terminal. 


### Project 3 - Rotary Encoder

1. Copy `code.py` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program.
2. Rotate the know either clockwise or counterclockwise, and try pressing down on the knob. 


### Project 4 - Buzzer

1. Copy `code.py` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program.
2. Music should start playing immediately. 


### Project 5 - OLED Display

1. Copy all files from `project_5_oled_display` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program. 
2. The display will be showing the message.


### Project 6 - PDM Microphone

1. Copy `code.py` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program. 
2. Enable plotter in Mu Editor after reloading the program. 
3. Proceed to speak or make sound near the mic module and observe the waveform change on your screen.


### Project 7 - Digital PIR Sensor

1. Copy `code.py` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program. 
2. The terminal shows the message whether motion detected or if motion stopped of a human. 


### Project 8 - IMU Sensor

1. Copy all files from `project_8_imu_sensor` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program. 
2. Move the board around. 
3. Enable the plotter in Mu Editor. Watch raw values and the plotter change based on the movement of the board. 


### Project 9 - Magnetometer

1. Copy all files from `project_9_magnetometer` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program. 
2. Move the board around. Or have some sort of magnetic accessory move around the sensor. 
3. Enable the plotter in Mu Editor. Watch raw values and the plotter change based on the movement of the board. 


### Project 10 - Digital Optical Sensor

1. Copy all files from `project_10_digital_optical_sensor` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program. 
2. Currently one of the library is missing, thus code does not compile.


### Project 11 - Temperature & Humidity Sensor

1. Copy all files from `project_11_temperature_himidity_sensor` in `CIRCUITPY` and now head to Mu Editor, click on `Ctrl + D` to reload the program.
2. Watch the logs print the temperature and humidity values on the screen.