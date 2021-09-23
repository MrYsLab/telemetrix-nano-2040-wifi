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

import sys
import time

from tmx_nano2040_wifi import tmx_nano2040_wifi

# Blink each of the colors of the onboard RGB LED.

# pin numbers for the LEDs
LED_G = 25  # green
LED_B = 26  # blue
LED_R = 27  # red

# Create a Telemetrix instance.
board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.246')

# RGB pins are already established as outputs in the Arduino sketch.
# Blink each LED twice.

board.set_pin_mode_digital_output(LED_G)
board.set_pin_mode_digital_output(LED_B)
board.set_pin_mode_digital_output(LED_R)

for pin in range(LED_G, LED_R+1):
    for blink in range(2):
        try:
            board.digital_write(pin, 1)
            time.sleep(1)
            board.digital_write(pin, 0)
            time.sleep(1)
        except KeyboardInterrupt:
            board.shutdown()
            sys.exit(0)

board.shutdown()
sys.exit(0)