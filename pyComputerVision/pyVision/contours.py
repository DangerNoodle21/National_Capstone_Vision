

"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit


"""

"""

    Threshhold Creation - Parameters:

        src – Source 8-bit single-channel image.

        dst – Destination image of the same size and the same type as src .

        maxValue – Non-zero value assigned to the pixels for which the condition is satisfied - MAX PIXEL VAULE FOR IMAGE

        adaptiveMethod – Adaptive thresholding algorithm to use, ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C . See the details below.

        thresholdType – Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV .

        blockSize – Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.

        C – Constant subtracted from the mean or weighted mean (see the details below). Normally, it is positive but may be zero or negative as well.

"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Unlimited Capture --> 0

def take_picture():

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    cv2.imwrite('Picture1.png', takePic1)
    print("Picture Taken and Saved.")


    #read image from file, finds out height and width, turns it into gray scale, assigns new name
    picture_1 = cv2.imread('Picture1.png', 1)
    height, width = picture_1.shape[0:2]
    gray = cv2.cvtColor(picture_1, cv2.COLOR_RGB2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow("Binary", thresh)



    
    

    _, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    picture_1COPY = picture_1.copy()
    index = -1
    thickness = 4
    color = (0, 255, 0)

    cv2.drawContours(picture_1COPY, contours, index, color, thickness)
    cv2.imshow("Contours", picture_1COPY)


cv2.namedWindow("Video")

while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=1, fy=1)
    cv2.imshow("Video", frame)

    ch2 = cv2.waitKey(1)
    if ch2 & 0xFF == ord('p'):
        take_picture()
    elif ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

