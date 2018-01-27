
"""

Press 'p' to take a picture from stream

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Video Camera Scource - 0

def keyboard():
    ret, picture_1 = cap.read()
    print("Pressed")
    cv2.namedWindow("Picture")
    picture_1 = cv2.resize(picture_1, (0,0), fx=1, fy=1)
    cv2.imshow("Picture", picture_1)


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
