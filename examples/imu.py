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

 DHT support courtesy of Martyn Wheeler
 Based on the DHTNew library - https://github.com/RobTillaart/DHTNew
"""

import sys
import time

from tmx_nano2040_wifi import tmx_nano2040_wifi


# Enable the IMU for 5 seconds, then disable it for 5 seconds,
# enable again for 5 seconds and exit.

def the_callback(data):
    print(f'IMU_REPORT: AX={data[1]} AY={data[2]} AZ={data[3]} GX={data[4]}, GY='
          f'{data[5]}, GZ={data[6]}')


# Create a Telemetrix instance.
board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.174')
try:

    # set the pin mode to imu, establish the callback
    # data should appear in the console
    board.set_pin_mode_imu(callback=the_callback)

    # let run for 5 seconds
    time.sleep(5)
    board.set_pin_mode_imu(callback=the_callback, enable=False)
    time.sleep(5)

    board.set_pin_mode_imu(callback=the_callback)
    time.sleep(5)

    board.shutdown()
    sys.exit(0)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
