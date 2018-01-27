
import cv2
import numpy as np


cap = cv2.VideoCapture(0) # Indicates the Camera

cv2.namedWindow("Video")


while(True):

    #Takes Picture and saves it, writes to console
    ret, takePic1 = cap.read()
    
    #Converts picture into grey scale image
    takePic1 = cv2.cvtColor(takePic1, cv2.COLOR_RGB2GRAY)

    thresh = 160
    ret, takePic1 = cv2.threshold(takePic1, thresh, 255, cv2.THRESH_BINARY)

    #Bluring the image, Gaussian
    takePic1 = cv2.GaussianBlur(takePic1, (3,3),0)


    adapt_thresh = cv2.adaptiveThreshold(takePic1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    blur_p1, contours, hierarchy = cv2.findContours(adapt_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    filtered = []
    
    for c in contours:
        if cv2.contourArea(c) < 1000:
            continue
        elif cv2.contourArea(c) > 3000:
            continue
        else:
            filtered.append(c)
    print(len(filtered))

    objects = np.zeros([takePic1.shape[0], takePic1.shape[1],3], 'uint8')


    for c in filtered:
       


        #Draws and outline around the contour, green
        cv2.drawContours(objects, [c], -1, (0,255,0), 3)

        
        #Centriod
        # Had to add +1 to advoid Dividion by Zero erro
        M = cv2.moments(c)
        cx = int( M['m10']/(M['m00'] + 1))
        cy = int( M['m01']/(M['m00'] + 1))

        #Centriods
        cv2.circle(objects, (cx,cy), 4, (0, 0, 255), -1)
        #Area and Perimter
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)

        print("(X,Y): ", cx, cy, "Area: ", area, "Perimter: ", perimeter)
    
    cv2.imshow("Video", adapt_thresh)


    cv2.imshow("Objects", objects)


    ch2 = cv2.waitKey(1)
    if ch2 & 0xFF == ord('p'):
        take_picture()
    elif ch2 & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
