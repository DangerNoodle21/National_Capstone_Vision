from __future__ import print_function
from cv_objs import CV
from cv_objs import FPS
from cv_objs import UI
from cv_objs import WebcamVideoStream
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i2c", "--i2c", type=int, default=0x04,
	help="Custom I2C address for distance data")

ap.add_argument("-t", "--target", type=int, default=1,
	help="Target Choice: 1 ==> Power Cube")
args = vars(ap.parse_args())

def main():

    compVision = CV.computerVision(args["target"], args["i2c"])
    threaded_stream = WebcamVideoStream(src=0).start()

    while(True):
        vid_stream = threaded_stream.read()
        vid_stream = imutils.resize(vid_stream, width=400)
        processed = compVision.comp_vision_start(vid_stream)

        cv2.imshow("Threaded / Processed Video", processed)
    
        ch2 = cv2.waitKey(1)
        if ch2 & 0xFF == ord('q'):
            break
    # do a bit of cleanup
    cv2.destroyAllWindows()
    threaded_stream.stop()


#If Statement to call main function
if __name__ == '__main__':
    main()
