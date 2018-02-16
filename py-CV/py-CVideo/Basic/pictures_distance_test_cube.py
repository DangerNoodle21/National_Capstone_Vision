
import cv2
import numpy as np




takePic1 = cv2.imread('cube1.jpg')


pic_gauss = cv2.GaussianBlur(takePic1, (1,1),0)
    
hsv = cv2.cvtColor(pic_gauss, cv2.COLOR_BGR2HSV)
    
lower_yellow = np.array([21,39,119])
upper_yellow = np.array([180,255,255])
    
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
          
cube_canny = cv2.Canny(mask, 50, 200, None, 3)

#Finds the Contours in frame taken, then prints the amount it finds
_, contours, hierarchy = cv2.findContours(cube_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

#Array for storing flitered Contours
filtered = []
 
#For loop for filtering out contours based on pixel Area
for c in contours:
    if cv2.contourArea(c) < 100:
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
    print(c_num, width/height)


cv2.imshow("Video", takePic1)