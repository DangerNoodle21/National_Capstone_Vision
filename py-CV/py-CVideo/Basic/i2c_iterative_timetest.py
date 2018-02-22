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

    list_make = []
  

    choice = input("1 = Byte, 2 = block: ")

    for x in range(10):
        num = random.randint(1, 9999)
        list_make.append(num)
    
    if choice == "1":
        for y in range(10):
            print(list_make[y])
            counter = int(len(str(list_make[y])))
            for i in range(counter):
                send_regular(int(ord(str(list_make[y]))))
                time.sleep(.1)

    elif choice == "2":
        for y in range(10):
            print(list_make[y])
            list_send = list(str(list_make[y]))
            for i in list_send:
                send_w_wrapper(int(ord(i)))
                time.sleep(.1)
    else:
        print("No Choice")


if __name__ == '__main__':
    main()