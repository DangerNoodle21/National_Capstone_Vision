
"""
In this code:


1. Filtering Color based up HSV values
2. Identifying Shapes - Squares



Press 'q' to quit


"""


import cv2
import numpy as np
import math
import sys


#Starts Video Stream, Number is the Video Scource
video_cap = cv2.VideoCapture(0)


#Funtion to start Video While Loop
def videoStream():

    while(True):
        #Pulls image from stream
        ret, video_stream = video_cap.read()

        cv2.imwrite('video_stream.png', video_stream)
        print("Picture Taken and Saved.")


        lower_white = np.array([0,0,167])
        upper_white = np.array([180,255,255])


        #read image from file, finds out height and width
        video_stream_png = cv2.imread('video_stream.png', 1)

        #Converts picture_1 to HSV image, Hue saturation
        hsv_frame = cv2.cvtColor(video_stream_png, cv2.COLOR_BGR2HSV)

        hsv_mask = cv2.inRange(hsv_frame, lower_white, upper_white)

        blur_mask = cv2.GaussianBlur(hsv_mask, (3,3),0)

        canny_video = cv2.Canny(video_stream, 50, 200, None, 3)


        #Finds the Contours in frame taken, then prints the amount it finds
        _, contours, hierarchy = cv2.findContours(canny_video, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))

        #Array for storing flitered Contours
        filtered = []
        upper = 0.1
        lower = 0.08


        #For loop for filtering out contours based on pixel Area
        for c in contours:
            M = cv2.moments(c)
            x,y,w,h = cv2.boundingRect(c)
            aspect_ratio = float(w)/h
            if aspect_ratio > 1.39:
                continue
            elif aspect_ratio < 1.36:
                continue
            else:
                filtered.append(c)
        print(len(filtered))

        objects = np.zeros([canny_video.shape[0], canny_video.shape[1],3], 'uint8')

        
        #For Loop for Filtering Contours - C the number of filtered countours in the array Filtered[]
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
            #area = cv2.contourArea(c)
            #perimeter = cv2.arcLength(c, True)

            x,y,w,h = cv2.boundingRect(c)
            a_r = float(w)/h

            cv2.rectangle(video_stream,(x,y),(x+w,y+h),(0,255,0),2)


            print(a_r)


        cv2.imshow("Video", video_stream)
        #Picture / Break if statement
        ch2 = cv2.waitKey(1)
        if ch2 & 0xFf == ord('q'):
            break


#def distComparison():
   # x= 12

#Function to end video capture and close the windows
def endVideo():
    video_cap.release()
    cv2.destroyAllWindows()

#Main Function
def main():
    videoStream()
    endVideo()

#If Statement to call main function
if __name__ == '__main__':
    main()
