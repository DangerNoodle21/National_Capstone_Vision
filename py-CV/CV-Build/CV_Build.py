from __future__ import print_function
from cv_objs import *
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())


# grab a pointer to the video stream and initialize the FPS counter
print("[INFO] sampling frames from webcam...")
stream = cv2.VideoCapture(0)
fps = FPS().start()




def main():

    vidstream = CAM.WebcamVideoStream()

    compVision = computerVision()
    compVision.comp_vision_start()


#If Statement to call main function
if __name__ == '__main__':
    main()
