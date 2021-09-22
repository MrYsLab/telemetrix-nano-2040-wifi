"""
 Copyright (c) 2021 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,f
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""

# Fade the 3 colors of the onboard RGB LED.

import sys
import time

from tmx_nano2040_wifi import tmx_nano2040_wifi

# pin numbers for the LEDs
LED_G = 25  # green
LED_B = 26  # blue
LED_R = 27  # red
# Create a Telemetrix instance.
board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.246')

# For RGB control, the pin mode must be set as output and
# performed in the setup function of the Arduino sketch. This
# is already being done in Telemetrix4Connect2040.

# NOTE: a value of 0 is maximum brightness and 255 is minimum brightness.
# 255 does not extinguish the LED and so
try:
    # cycle through the 3 LEDs.
    for pin in range(25, 28):
        for i in range(255, -1, -1):
            board.analog_write(pin, i)
            time.sleep(.005)
        time.sleep(1)

        for i in range(255):
            board.analog_write(pin, i)
            time.sleep(.005)
        board.digital_write(pin, 0)
    board.set_pin_mode_digital_output(LED_G)
    board.digital_write(LED_G, 1)
    board.digital_write(LED_G, 0)

    board.set_pin_mode_digital_output(LED_B)
    board.digital_write(LED_B, 1)
    board.digital_write(LED_B, 0)
    board.set_pin_mode_digital_output(LED_R)
    board.digital_write(LED_R, 1)
    board.digital_write(LED_R, 0)
    board.shutdown()
    sys.exit(0)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
