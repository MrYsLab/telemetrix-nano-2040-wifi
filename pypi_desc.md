# Telemetrix-Nano-2040-WiFi

Telemetrix-Nano-2040-WiFi is a member of the [Telemetrix](https://mryslab.github.io/telemetrix/) 
family and is a Python client
specifically tailored to remotely control and monitor
an Arduino Nano RP2040 Connect using Python scripts running on your PC.

When paired with the [Telemetrix4Connect2040](https://github.com/MrYsLab/Telemetrix4Connect2040)
custom Arduino server sketch, control and
monitoring of the Arduino Nano RP2040 Connect is accomplished using a Wi-Fi link 
between the
PC and the Arduino.

This library supports the following features:
* Analog and Digital Input
* Digital Outputs including PWM
* Onboard devices:
    * IMU
    * Microphone
    * RGB LED
* I2C device communications.
* SPI device communications.
* HC-SR04 Type distance sensors.
* DHT Type humidity/temperature sensors.
* Servo motors.
* NeoPixel strips.


A [User's Guide](https://mryslab.github.io/telemetrix-nano-2040-wifi/) explaining installation and use is available online.

The Python API for may be found [here.](https://htmlpreview.github.io/?https://github.com/MrYsLab/telemetrix-nano-2040-wifi/blob/master/html/tmx_nano2040_wifi/index.html) 


Here is a sample project that blinks the Arduino Board LED:

```
import sys
import time

from tmx_nano2040_wifi import tmx_nano2040_wifi

"""
Blink the board LED.
"""

# some globals
DIGITAL_PIN = 13  # the board LED

# Create a Telemetrix instance.
board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.246')

# Set the DIGITAL_PIN as an output pin
board.set_pin_mode_digital_output(DIGITAL_PIN)

# Blink the Board LED
for blink in range(3):
    # When hitting control-c to end the program
    # in this loop, we are likely to get a KeyboardInterrupt
    # exception. Catch the exception and exit gracefully.
    try:
        print('1')
        board.digital_write(DIGITAL_PIN, 1)
        time.sleep(1)
        print('0')
        board.digital_write(DIGITAL_PIN, 0)
        time.sleep(1)
    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)
board.shutdown()
sys.exit(0)
```