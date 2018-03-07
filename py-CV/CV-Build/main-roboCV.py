from __future__ import print_function
import cv2
import imutils
from cv_objs import UI
from cv_objs import CV
from cv_objs import CAM_STREAM
import argparse




ap = argparse.ArgumentParser()

ap.add_argument("-i2c", "--I2C", type=bool, default=False,
	help="Turn on I2C Connection")

ap.add_argument("-add", "--i2C_Address", type=int, default=0x04,
	help="To change the address of the I2C data, default is 0x04")

ap.add_argument("-UI", "--userInter", type=bool, default=True,
	help="To turn off UI elements")

ap.add_argument("-t", "--target", type=int, default=1,
	help="Target Choice: 1 ==> Power Cube")

args = vars(ap.parse_args())

def main():

    vs = CAM_STREAM.CAM_STREAM(0).start()

    compVision = CV.computerVision(args["target"])

    if args["I2C"]:
        from cv_objs.I2C import I2C
        i2c_obj = I2C.I2C(args["i2C_Address"])

    user_Inter = UI.userInterface()


    while(True):
        #Grabs Video Stream
        vid_stream = vs.read()

        #Processes Video, Return Array hold contour data, processed video
        console_Array, processed_vid = compVision.comp_vision_start(vid_stream)

        #Adding UI elements

        if args["userInter"]:
            user_Inter.draw_UI_elements(console_Array, processed_vid)

        #If enabled, send I2C data
        if args["I2C"]:
            i2c_obj.send_I2C_data(console_Array)

        #Resizing Video
        processed_vid = imutils.resize(processed_vid, width=250)

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
