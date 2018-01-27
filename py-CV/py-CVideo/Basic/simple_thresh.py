
"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Video Scource

def keyboard():

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    cv2.imwrite('Picture1.png', takePic1)
    print("Picture Taken and Saved.")

    #Reads image from file, turns it Black and white(Zero Color Channels), gets dimenstions
    picture_1 = cv2.imread('Picture1.png', 0)
    height, width = picture_1.shape[0:2]

    #Creates names window, shows picture taken - Before
    cv2.namedWindow("Picture")
    cv2.imshow("Picture", picture_1)
   
    #Thresh hold values, creates thresh hold image from one taken - After
    thresh = 150
    ret, thresh = cv2.threshold(picture_1, thresh, 255, cv2.THRESH_BINARY)
    cv2.imshow("CV THRESH", thresh)

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

