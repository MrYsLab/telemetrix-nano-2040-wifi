# Pin Modes
Before utilizing a pin, you must set its pin mode. Check the APIs for methods that 
begin with _set_pin_mode_ in their name for the available modes.

# Specifying Pin Numbers

## Digital Pin Numbers
Digital pin-numbers are specified using a single integer value, such as 3 for digital 
pin 3.

### Analog Pin Numbers
Analog pin-numbers are also specified using a single integer value using the analog 
pin-number without the "A." For example, pin A4 is identified simply as 4.

## SPI Pins
Telemetrix uses the standard SPI pins. Only the chip select pins need to be specified.

    (CIPO) - D12
    (COPI) - D11
    (SCK) - D13
    (CS/SS) - Any GPIO (except for A6/A7)



## I2C Pins
Telemetrix uses the standard I2C pins.

    (SDA) - A4
    (SCL) - A5

