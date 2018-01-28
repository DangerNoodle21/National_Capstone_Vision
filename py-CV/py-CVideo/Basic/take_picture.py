
"""
In this code:

1. Takes picture with keyboard press
2. Writes Words picture takes
3. Clicking Puts a circle on the Screen


Press 'p' to take a picture from stream

Press 'q' to quit


"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Video Camera Scource - 0

def keyboard():

    #Keyboard Function

    #Reads Video, names capture picture_1, outputs to console
    ret, picture_1 = cap.read()
    print("Pressed")

    #Creates Named window, Resizes the pictures, add text, Shows picture
    cv2.namedWindow("Picture_1")
    picture_1 = cv2.resize(picture_1, (0,0), fx=1, fy=1)

    #Adds Text to picture
    cv2.putText(picture_1, 'ADD TEXT', (210, 240), font, 4, (0,255,0), 4, cv2.LINE_AA)
    cv2.imshow("Picture_1", picture_1)

#Circle Parameters for click function
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)
font = cv2.FONT_HERSHEY_SIMPLEX

# Function Click
def click(event, x, y, flags, param):
    #Global variable 
    global point, pressed

    #Event Handler for click, left mouse button down
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #Prints to console, then changed Point Coordinates
        print("Pressed", x, y)
        point = (x, y)

# Named Window and Call backing event handler for mouse click
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", click)

#Video Loop
while(True):
     
    #video Capture
    ret, frame = cap.read()
        
    #Resize Frame
    frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)

    #Draw Circle Function
    cv2.circle(frame, point, radius, color, line_width)

    #
    cv2.imshow("Video", frame)


    #Picture / Break if statement
    ch2 = cv2.waitKey(1)
    if ch2 & 0xFF == ord('p'):
        keyboard()
    elif ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
