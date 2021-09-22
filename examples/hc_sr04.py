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
This is an example program for HC-SR04 type distance sensors.

A single device was tested.
"""

# some globals
TRIGGER_PIN = 11
ECHO_PIN = 12

# indices into callback data
TRIGGER = 1
DISTANCE_IN_CENTIMETERS = 2
TIME_STAMP = 3


def the_callback(data):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[TIME_STAMP]))

    print(f'{date}\t Trigger Pin::\t{data[TRIGGER]}\t Distance(cm):\t'
          f'{data[DISTANCE_IN_CENTIMETERS]}')


# Create a Telemetrix instance.
board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.246')
try:
    # instantiate HC-SR04 devices
    board.set_pin_mode_sonar(TRIGGER_PIN, ECHO_PIN, the_callback)

    while True:
        try:
            # do nothing but sleep while the reports come in.
            time.sleep(1)
        except KeyboardInterrupt:
            board.shutdown()
            sys.exit(0)

except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
