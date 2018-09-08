import smbus2
import time


class I2Cinterface:

    #Raspberry Pi Bus / Slave Address for sending

    def __init__(self, end_address):
        self.rpi_bus = smbus2.SMBus(1)
        self.I2C_slave_address = end_address

    #To find if array is empty or not
    def Enquiry(self,lis1):
        if len(lis1) == 0:
            return False
        else:
            return True


    def send_I2C_bit(self, byte):
        self.rpi_bus.write_byte(self.I2C_slave_address, byte)

    def convert_Number(self, number):
        #Converts to String, then puts it in a list
        list_send = list(str(int(number)))

        #Iterates through list, and sends the number with a 0.01 second delay
        for i in list_send:
            #Converts to Unicode, then to int
            self.send_I2C_bit(int(ord(i)))
            time.sleep(.01)


    #Send Int to predefined I2C address
    def send_I2C_data(self, console_array):

        if self.Enquiry(console_array):

            c_num, distance, (cx, cy) = console_array[0]

            self.convert_Number(distance)

        else:
            self.convert_Number(0)
