
"""

Click in the window to move the cirle to another point

Press 'q' to quit



"""
import cv2
import scipy
import matplotlib
import numpy as np


cap = cv2.VideoCapture(0) # Capture Unlimted frames


#Circle Parameters
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)
font = cv2.FONT_HERSHEY_SIMPLEX

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Pressed", x, y)
        point = (x, y)

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", click)

while(True):
    
    ret, frame = cap.read()
    
    ch = cv2.waitKey(1) # 1 - Waits 1 mils to run loop again

    cv2.putText(frame, 'test', (210, 240), font, 4, (0,255,0), 4, cv2.LINE_AA)
   
    frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)
    
    cv2.imshow("frame", frame)
    
    
    if ch & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
