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
Monitor a digital input pin with pullup enabled
"""

"""
Setup a pin for digital input and monitor its changes
"""

# Callback data indices
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3


def the_callback(data):
    """
    A callback function to report data changes.
    This will print the pin number, its reported value and
    the date and time when the change occurred

    :param data: [pin mode, pin, current reported value, pin_mode, timestamp]
    """
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
    print(f'Report Type: {data[CB_PIN_MODE]} Pin: {data[CB_PIN]} '
          f'Value: {data[CB_VALUE]} Time Stamp: {date}')


board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.246')
board.set_pin_mode_digital_input_pullup(11, the_callback)

try:
    print('Reporting enabled for 5 seconds.')
    time.sleep(5)
    print('Disabling reporting for 3 seconds.')
    board.disable_digital_reporting(11)
    time.sleep(3)
    print('Re-enabling reporting.')
    board.enable_digital_reporting(11)
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
