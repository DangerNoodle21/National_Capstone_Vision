


"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Unlimited Capture --> 0

def take_picture():

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    cv2.imwrite('Picture1.png', takePic1)
    print("Picture Taken and Saved.")


    #read image from file, finds out height and width
    picture_1 = cv2.imread('Picture1.png', 1)
    height, width = picture_1.shape[0:2]

    #Converts picture into grey scale image
    gray = cv2.cvtColor(picture_1, cv2.COLOR_RGB2GRAY)

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
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    # Showing Thresh - Pictures
    cv2.imshow("Binary", thresh)

    thresh = 150
    ret, users_thesh = cv2.threshold(picture_1, thresh, 255, cv2.THRESH_BINARY)
    cv2.imshow("CV THRESH", thresh)

    #Contours Commands - (Contous - List of points which surrounds an object) 
    _, contours, hierarchy = cv2.findContours(users_thesh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Deep Copy
    Copy_Picture = picture_1.copy()
    index = -1
    thickness = 4
    color = (255, 0 , 255)

    objects = np.zeros([picture_1.shape[0], picture_1.shape[1],3], 'uint8')
    for c in contours:
        cv2.drawContours(objects, [c], -1, color, -1)

        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)

        M = cv2.moments(c)
        cx = int( M['m10']/M['m00'])
        cy = int( M['m01']/M['m00'])
        cv2.circle(objects, (cx,cy), 4, (0,0,255), -1)

        print("Area: {}, perimeter: {}".format(area,perimeter))


   


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

