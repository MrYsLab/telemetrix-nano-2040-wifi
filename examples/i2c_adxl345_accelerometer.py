"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
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
This example sets up and control an ADXL345 i2c accelerometer.
It will continuously print data the raw xyz data from the device.
"""


# the call back function to print the adxl345 data
def the_callback(data):
    """
    Data is supplied by the library.
    :param data: [report_type, Device address, device read register,
    number of bytes returned, x data pair, y data pair, z data pair
    time_stamp]
    """

    time_stamp = data.pop()
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))
    print(f'Raw Data:  {data}')
    print(f'ADXL345 Report On: {date}: ')
    print(f'\t\t x-pair={data[4]}, '
          f'{data[5]}  y-pair={data[6]}, '
          f'{data[7]} z-pair={data[8]}, '
          f'{data[9]}')
    print()


def adxl345(my_board):
    # setup adxl345
    # device address = 83
    my_board.set_pin_mode_i2c()

    # set up power and control register
    my_board.i2c_write(83, [45, 0])
    time.sleep(.1)
    my_board.i2c_write(83, [45, 8])
    time.sleep(.1)

    # set up the data format register
    my_board.i2c_write(83, [49, 8])
    time.sleep(.1)
    my_board.i2c_write(83, [49, 3])
    time.sleep(.1)

    # read_count = 20
    while True:
        # read 6 bytes from the data register
        try:
            my_board.i2c_read(83, 50, 6, the_callback)
            time.sleep(.1)

        except (KeyboardInterrupt, RuntimeError):
            my_board.shutdown()
            sys.exit(0)


board = tmx_nano2040_wifi.TmxNano2040Wifi(ip_address='192.168.2.174')
try:
    adxl345(board)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
