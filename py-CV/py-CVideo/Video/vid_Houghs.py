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

        lower_white = np.array([0,0,181])
        upper_white = np.array([180,59,255])


        #Pulls image from stream
        ret, video_stream = video_cap.read()

        hsv_frame = cv2.cvtColor(video_stream, cv2.COLOR_RGB2GRAY)

        #hsv_mask = cv2.inRange(hsv_frame, lower_white, upper_white)

        #blur_mask = cv2.GaussianBlur(hsv_mask, (3,3),0)

        canny_video = cv2.Canny(video_stream, 100, 200, None, 3)

        # Copy edges to the images that will display the results in BGR
        cdstP = cv2.cvtColor(hsv_frame, cv2.COLOR_GRAY2BGR)
        cdstH = cv2.cvtColor(hsv_frame, cv2.COLOR_GRAY2BGR)
        #  Standard Hough Line Transform
        linesH = cv2.HoughLines(canny_video, 1, np.pi / 180, 100, None, 2, 10)

        linesP = cv2.HoughLinesP(canny_video, 1, np.pi / 180, 1, None, 1, 2)

         # Draw the lines
        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)



                # Draw the lines
        if linesH is not None:
            for i in range(0, len(linesH)):
                rho = linesH[i][0][0]
                theta = linesH[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                cv2.line(cdstH, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)


        cv2.imshow("Houghs-P", cdstP)
        cv2.imshow("Hough-H", cdstH)



        #Picture / Break if statement
        ch2 = cv2.waitKey(1)
        if ch2 & 0xFf == ord('q'):
            break

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