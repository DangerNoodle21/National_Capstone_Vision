import smbus2
import numpy as np
import time
import random

rpi_bus = smbus2.SMBus(1)
rpi_wrapper = smbus2.SMBusWrapper(1)



slave_add = 0x04

def send_w_wrapper(number):
    with smbus2.SMBusWrapper(1) as bus:
        bus.write_i2c_block_data(slave_add, 0, number)

def send_regular(number):
    rpi_bus.write_byte(slave_add, number)


def main():

    list_1 = []

    choice = input("1 = Byte, 2 = block: ")

    for x in range(0, 10):
        num = random.randint(1, 9999)
        list_1.append(num)
    
    if choice == "1":
        for y in range(0, 10):
            print(list_1[y])
            send_regular(list_1[y])
            time.sleep(.2)

    elif choice == "2":
        for y in range(0, 10):
            print(list_1[y])
            send_w_wrapper(list_1)
            time.sleep(.2)
    else:
        print("No Choice")


if __name__ == '__main__':
    main()