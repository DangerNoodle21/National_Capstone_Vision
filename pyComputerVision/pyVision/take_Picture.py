
"""
Press 'p' to take a picture from stream

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Unlimited Capture --> 0

def click():
    ret, picture_1 = cap.read()
    print("Pressed")
    cv2.namedWindow("Picture")
    picture_1 = cv2.resize(picture_1, (0,0), fx=1, fy=1)
    cv2.imshow("Picture", picture_1)

color_square = (0,255,0)
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
