"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

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

 DHT support courtesy of Martyn Wheeler
 Based on the DHTNew library - https://github.com/RobTillaart/DHTNew
"""

import sys
import time

from tmx_nano2040_wifi import tmx_nano2040_wifi


def the_callback(data):
    print(f'MICROPHONE_REPORT: channel type: {data[2]}  Value = {data[1]}')


# Create a Telemetrix instance.
board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.174')

try:
    # Set the DIGITAL_PIN as an output pin
    board.set_pin_mode_microphone(callback=the_callback)

    # listen for 5 seconds
    time.sleep(5)

    print('Turning mic off')
    board.set_pin_mode_microphone(enable=False)
    time.sleep(5)
    # wait 5 seconds before turning mic back on
    print('Mic is back on, program will exit in 5 seconds')
    board.set_pin_mode_microphone(callback=the_callback)
    time.sleep(5)
    board.shutdown()
    sys.exit(0)

except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)

