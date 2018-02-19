
import smbus2
import time


class I2C(object):

    #Raspberry Pi Bus / Slave Address for sending
    rpi_bus = smbus2.SMBus(1)
    I2C_slave_address = 0x04
    rpi_wrapperBus = smbus2.SMBusWrapper(1)

    def __init__(self, address):
        self.arduino_address = address

    def write_I2C_byte(number):
        rpi_wrapperBus.write_byte(I2C_slave_address, 0, number)

    def write_I2C_32Byte(number):
        rpi_wrapperBus.write_i2c_block_data(I2C_slave_address, 0, number)
