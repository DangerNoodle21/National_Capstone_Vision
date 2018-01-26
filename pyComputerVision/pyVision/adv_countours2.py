



"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit



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


    #read image from file, finds out height and width
    picture_1 = cv2.imread('Picture1.png', 1)

    #Converts picture1 into grey scale image
    pic1_gray = cv2.cvtColor(picture_1, cv2.COLOR_RGB2GRAY)

    adapt_thres = cv2.adaptiveThreshold(pic1_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    _, contours, hierarchy = cv2.findContours(adapt_thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    index = -1
    thickness = 4
    color = (0, 255, 0)

    cv2.drawContours(adapt_thres, contours, index, color, thickness)
    cv2.imshow("adapt_thres", adapt_thres)

    # Array to stores the countour data from above
    objects = np.zeros([picture_1.shape[0], picture_1.shape[1], 3], 'uint8')


    for c in contours:
        cv2.drawContours(objects, [c], -1, color, -1)

        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)

        
      
        #draws dots in middle
        # Had to add +1 to advoid Dividion by Zero erro
        M = cv2.moments(c)
        cx = int( M['m10']/(M['m00'] + 1))
        cy = int( M['m01']/(M['m00'] + 1))

        #Centriods
        cv2.circle(objects, (cx,cy), 1, (0, 0, 255), -1)
        
        #Prints the area in Pixels of the found contours
        print("Area: {}, perimeter: {}".format(area, perimeter))


    cv2.imshow("Objects", objects)
        

   


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

