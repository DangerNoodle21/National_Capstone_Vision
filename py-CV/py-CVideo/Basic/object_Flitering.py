


"""
Press 'p' to take a picture from stream

Will make thresh hold comparison

Press 'q' to quit
"""

import cv2
import numpy as np
import random


cap = cv2.VideoCapture(0) # Video Scouce

def keyboard():

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    cv2.imwrite('Picture1.png', takePic1)
    print("Picture Taken and Saved.")

    #read image from file, finds out height and width
    picture_1 = cv2.imread('Picture1.png', 1)

    #Converts picture into grey scale image
    gray_p1 = cv2.cvtColor(picture_1, cv2.COLOR_RGB2GRAY)

    #Bluring the , Gaussian Blur
    blur_p1 = cv2.GaussianBlur(gray_p1, (3,3),0)

    #Adaptive Threshold - After the blur
    adapt_thresh = cv2.adaptiveThreshold(blur_p1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 205, 1)
    
    #Finding Contours and printing unflitered count
    _, contours, _ = cv2.findContours(adapt_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    #Array for flitered contours
    filtered = []
    
    #For loop, c number contours from the array Contours ^^, 

    #Fliteres out contours:
        #Less than num. for PIXEL area
        #Then Prints out the filtered amount
    for c in contours:
        if cv2.contourArea(c) < 2200:
            continue
        elif cv2.contourArea(c) > 2500:
            continue
        else:
            filtered.append(c)
    print(len(filtered))


    #New Object array filled with 0's
    objects = np.zeros([picture_1.shape[0],picture_1.shape[1],3], 'uint8')


    for c in filtered:

        #Random Color
        col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        #Fills in the countour with a random color
        cv2.drawContours(objects,[c], -1, col, -1)

        #Draws and outline around the contour, green
        cv2.drawContours(objects, [c], -1, (0,255,0), 3)
        
        # X and Y for contour
        # Had to add +1 to advoid Dividion by Zero erro
        M = cv2.moments(c)
        cx = int( M['m10']/(M['m00'] + 1))
        cy = int( M['m01']/(M['m00'] + 1))

        #Centriods
        cv2.circle(objects, (cx,cy), 4, (0, 0, 255), -1)

        #Area and Perimter
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)

        #Console Print Relavent information
        print("(X,Y): ", cx, cy, "Area: ", area, "Perimter: ", perimeter)

    #Show Outside of For loop
    cv2.imshow("Contours_Filtering",objects)



   
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

