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

