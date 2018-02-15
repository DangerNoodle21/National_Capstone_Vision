
"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(1) # Unlimited Capture --> 0

def keyboard():

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    cv2.imwrite('Picture1.png', takePic1)
    print("Picture Taken and Saved.")

    #read image from file, finds out height and width
    picture_1 = cv2.imread('Picture1.png', 1)

    # Converts picture_1 to HSV image, Hue saturation
    hsv_p1 = cv2.cvtColor(picture_1, cv2.COLOR_BGR2HSV)


    # White is produced by specifying zero saturation and full value, regardless of hue
    res, hsv_thresh = cv2.threshold(hsv_p1[:,:,0], 120, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("hsv_thresh", hsv_thresh)

    hsv_edges = cv2.Canny(picture_1, 100, 70)
    cv2.imshow("hsv_edges", hsv_edges)


cv2.namedWindow("Video")


#Video Loop
while(True):

    #video Capture
    ret, frame = cap.read()

    #Resize Frame
    frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)
    cv2.imshow("Video", frame)


    #Picture / Break if statement
    ch2 = cv2.waitKey(1)
    if ch2 & 0xFF == ord('p'):
        keyboard()
    elif ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

