
"""
In this code:


1. Filtering Color based up HSV values
2. Identifying Shapes - Squares



Press 'q' to quit


"""


import cv2
import numpy as np

selection = input("Integrated Cam = 0, Usb = 1: ")
if selection == 0:
    mode = 0
elif selection == 1:
    mode = 1
else:
    mode = 0

#Starts Video Stream, Number is the Video Scource
video_cap = cv2.VideoCapture(mode)


#Funtion to start Video While Loop
def videoStream(mode):

    

    while(True):
        #Pulls image from stream
        ret, video_stream = video_cap.read()

        video_stream_gray = cv2.cvtColor(video_stream, cv2.COLOR_RGB2GRAY)


        blur_mask = cv2.GaussianBlur(video_stream_gray, (3,3),0)

        canny_video = cv2.Canny(video_stream, 50, 200, None, 3)


        #Finds the Contours in frame taken, then prints the amount it finds
        _, contours, hierarchy = cv2.findContours(canny_video, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))

        #Array for storing flitered Contours
        filtered = []
        upper = 0.1
        lower = 0.08

        c_num =0
        #For loop for filtering out contours based on pixel Area
        for c in contours:
            rect = cv2.minAreaRect(c)
            width_filter, height_filter = rect[1]
            if height_filter == 0:
                continue
            elif width_filter/height_filter > 1.41:
                continue
            elif width_filter/height_filter < 1.40:
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
            
            c_num = c_num + 1

            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(video_stream,[box],0,(0,0,255),2)
            width, height = rect[1]

            font = cv2.FONT_HERSHEY_SIMPLEX
            text = str(c_num)

            cv2.putText(video_stream, text, (cx, cy), font, 1, (0,255,0), 1, cv2.LINE_AA)

            #Using Focal Distance at know distance of 33'

            # Focal lenght = (Pixel Width x Distance) / Width
            # FL = (57.9 x 33') / 3' = 639.9

            # Distance = (Width x Focal Lenght) / Pixel Width

           
            distance = (3*639.9) / width
            
            print(c_num, width/height, "Distance:", distance)


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
   

    videoStream(mode)
    endVideo()

#If Statement to call main function
if __name__ == '__main__':
    main()
