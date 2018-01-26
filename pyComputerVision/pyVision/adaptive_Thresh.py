
"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Unlimited Capture --> 0

def click():

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    cv2.imwrite('Picture1.png', takePic1)
    print("Picture Taken and Saved.")


    #read image from file, turns it Black and white, gets dimenstions
    picture_1 = cv2.imread('Picture1.png', 0)
    height, width = picture_1.shape[0:2]

    #Creates names window, shows picture taken
    cv2.namedWindow("Picture")
    cv2.imshow("Picture", picture_1)
   
    #Thresh hold values, creates thresh hold image from one taken
    thresh = 85
    ret, thresh = cv2.threshold(picture_1, thresh, 255, cv2.THRESH_BINARY)
    cv2.imshow("CV THRESH", thresh)


cv2.namedWindow("Video")

while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=1, fy=1)
    cv2.imshow("Video", frame)

    ch2 = cv2.waitKey(1)
    if ch2 & 0xFF == ord('p'):
        click()
    elif ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

