import smbus2
import time


class I2C(object):

    #Raspberry Pi Bus / Slave Address for sending
    rpi_bus = smbus2.SMBus(1)
    I2C_slave_address = 0

    def __init__(self, end_address):
        self.I2C_slave_address = end_address

    def send_over_wire(self, byte):
        self.rpi_bus.write_byte(self.I2C_slave_address, byte)

    #Send Int to predefined I2C address
    def i2c_send_byte(self, number):

        #Converts to String, then puts it in a list
        list_send = list(str(int(number)))

        #Iterates through list, and sends the number with a 0.01 second delay
        for i in list_send:
            #Converts to Unicode, then to int
            self.send_over_wire(int(ord(i)))
            time.sleep(.01)