from __future__ import print_function
import cv2
import imutils
import argparse

from ObjectClasses import *





ap = argparse.ArgumentParser()

ap.add_argument("-i2c", "--I2C", type=int, default=0,
	help="Turn on I2C Connection")

ap.add_argument("-add", "--i2C_Address", type=int, default=0x04,
	help="To change the address of the I2C data, default is 0x04")

ap.add_argument("-ui", "--userInter", type=int, default=1,
	help="To turn off UI elements")

ap.add_argument("-t", "--target", type=int, default=1,
	help="Target Choice: 1 ==> Power Cube")

args = vars(ap.parse_args())

def main():
    uichoice = args["userInter"]
    i2cChoice = args["I2C"]
    i2cAdd = args["i2C_Address"]
    target = args["target"]

    videoIntake = c_CameraIntake.CameraIntake(0).start()
    objectProfile = c_ObjectProfiles.ObjectProfiles(target)
    userInterface = c_UserInterface.UserInterface()


    if i2cChoice:
        from ObjectClasses.c_I2Cinterface import I2Cinterface
        i2cObject = c_I2Cinterface.I2Cinterface(i2cAdd)


    while(True):
        #Grabs Video Stream
        videoStream = videoIntake.read()

        #Processes Video, Return Array hold contour data, processed video
        console_Array, processed_vid = objectProfile.comp_vision_start(videoStream)

        #Adding UI elements
        if uichoice == 1:
            userInterface.draw_UI_elements(console_Array, processed_vid)

        #If enabled, send I2C data
        if i2cChoice == 1:
            i2cObject.send_I2C_data(console_Array)

        #Resizing Video
        processesVideo = imutils.resize(processed_vid, width=250)

        #Showing Video
        cv2.imshow("Threaded / Processed Video", processed_vid)

        #Press Q to quit
        ch2 = cv2.waitKey(1)
        if ch2 & 0xFF == ord('q'):
            break


    #Clean up after quiting program
    cv2.destroyAllWindows()
    vs.stop()


#If Statement to call main function
if __name__ == '__main__':
    main()
