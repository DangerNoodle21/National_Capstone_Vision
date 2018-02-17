"""
In this code:



1. Adaptive Threshold 
2. Gass Blur
3. Contours
4. Contour filtering

End Output - This will find a 5' x 3' reflective tape square
    about 4 feet away from the camera

Press 'q' to quit


"""


import cv2
import numpy as np


cap = cv2.VideoCapture(1) # Video Scource

cv2.namedWindow("Video")


while(True):

    #Pulls image from stream
    _, takePic1 = cap.read()

    
    #Bluring the image, for easier ID, Gaussian Blur
    takePic1 = cv2.GaussianBlur(takePic1, (33,33),0)
    
    hsv = cv2.cvtColor(takePic1, cv2.COLOR_BGR2HSV)
    
    lower_yellow = np.array([0,34,0])
    upper_yellow = np.array([56,165,170])
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
          
    cube_canny = cv2.Canny(mask, 50, 200, None, 3)

    #Finds the Contours in frame taken, then prints the amount it finds
    _, contours, hierarchy = cv2.findContours(cube_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    #Array for storing flitered Contours
    filtered = []
 
    #For loop for filtering out contours based on pixel Area
    for c in contours:
        if cv2.contourArea(c) < 50:
            continue
        elif cv2.contourArea(c) > 30000:
            continue
        else:
            filtered.append(c)
    print(len(filtered))

    objects = np.zeros([takePic1.shape[0], takePic1.shape[1],3], 'uint8')
    c_num = 0
    #For Loop for Filtering Contours - C the number of filtered countours in the array Filtered[]
    for c in filtered:

        #Centriod
        # Had to add +1 to advoid Dividion by Zero erro
        M = cv2.moments(c)
        cx = int( M['m10']/(M['m00'] + 1))
        cy = int( M['m01']/(M['m00'] + 1))

        #Centriods
        cv2.circle(objects, (cx,cy), 4, (0, 0, 255), -1)
            
        c_num = c_num + 1

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(takePic1,[box],0,(0,0,255),2)
        width, height = rect[1]

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(c_num)

        cv2.putText(takePic1, text, (cx, cy), font, 1, (0,255,0), 1, cv2.LINE_AA)
        
        #Using Focal Distance at know distance of 33'

        # Focal lenght = (Pixel Width x Distance) / Width
        # FL = (196 x 34in) / 13 in = 512.61

        # Distance = (Width x Focal Lenght) / Pixel Width
        distance = (13 * 512.61) / width


        #Using Focal Distance at know distance of 33'
        print(c_num, width, height, distance)


    cv2.imshow("Video", takePic1)


    #cv2.imshow("Objects", objects)


    #Picture / Break if statement
    ch2 = cv2.waitKey(1)
    if ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
