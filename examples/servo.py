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
Attach a pin to a servo and move it about.
"""

# some globals
SERVO_PIN = 11


# Create a Telemetrix instance.
board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.246')
try:
    board.set_pin_mode_servo(SERVO_PIN, 1000, 2000)

    time.sleep(1)
    board.servo_write(SERVO_PIN, 90)
    time.sleep(1)
    board.servo_write(SERVO_PIN, 0)
    time.sleep(1)
    board.servo_write(SERVO_PIN, 180)
    time.sleep(1)
    board.servo_write(SERVO_PIN, 90)
    board.servo_detach(11)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)

board.shutdown()
sys.exit(0)


