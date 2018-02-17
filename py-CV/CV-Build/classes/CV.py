import numpy as np
import cv2
import curses
from classes import UI

class computerVision(object):

    #To find if array is empty or not
    def Enquiry(lis1):
        if len(lis1) == 0:
            return False
        else:
            return True
    #Computer Vision Profile for Power-Cube
    def cubeProfile(stream, filtered_contours):
        

        cube_blur  = cv2.GaussianBlur(stream, (33,33),0)
    
        hsv = cv2.cvtColor(cube_blur, cv2.COLOR_BGR2HSV)
    
        lower_yellow = np.array([0,34,0])
        upper_yellow = np.array([56,165,170])
    
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
          
        cube_canny = cv2.Canny(mask, 50, 200, None, 3)
 
          
        _, contours, hierarchy = cv2.findContours(cube_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Filtering with Aspect Ratio : 0.80139
        for c in contours:
            rect_filter = cv2.minAreaRect(c)
            width_filter, height_filter = rect_filter[1]
            if height_filter == 0:
                continue
            if width_filter  / height_filter < 0.1:
                continue
            elif width_filter  / height_filter > 0.7:
                continue
            else:
                filtered_contours.append(c)

        return filtered_contours

    #Computer Vision Profile for Practice Targeting Square   
    def targetSquareProfile(stream, filtered_contours):

        # Converts to gray scale / Adds Blur / Converts to CannyEdge Detection
        video_stream_gray = cv2.cvtColor(video_stream, cv2.COLOR_RGB2GRAY)
        video_stream_gray = cv2.GaussianBlur(video_stream_gray, (3,3),0)
        video_stream_gray = cv2.Canny(video_stream_gray, 50, 200, None, 3)


        #Finds the Contours in frame taken, then prints the amount it finds
        _, contours, hierarchy = cv2.findContours(video_stream_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        con_unFiltered = len(contours)

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

        return filtered
    
    #Main Computer Vision Program
    def comp_vision_start(stdscr):


        #Curses Display - Options
        curses.start_color(); curses.curs_set(0);
        
        

        #Creating console out boxes from UI
        consoleBoxes= UI.userInterface.outputBoxCreator(stdscr);


        stream = cv2.VideoCapture(1)
        
        while(True):

            #Array for storing filtered Contours / console array to send to console output
            filtered_contours = []
            console_Array = []

            #Contour Number for Identification
            c_num = 0

            ret, obj_stream  = stream.read()

            filtered_contours = computerVision.cubeProfile(obj_stream, filtered_contours)
          
            #Number of Filtered Contours
            con_filtered = len(filtered_contours)
            #Array for drawing contours
            objects = np.zeros([obj_stream.shape[0], obj_stream.shape[1],3], 'uint8')

            #For Loop for Filtering Contours - C the number of filtered contours in the array Filtered[]
            for c in filtered_contours:

                #Contour Number
                c_num = c_num + 1
                font = cv2.FONT_HERSHEY_SIMPLEX
                text = str(c_num)

                #Centroid
                # Had to add +1 to avoid Division by Zero error
                M = cv2.moments(c)
                cx = int( M['m10']/(M['m00'] + 1))
                cy = int( M['m01']/(M['m00'] + 1))

                #Centroids
                cv2.circle(objects, (cx,cy), 4, (0, 0, 255), -1)

                #Area of Found Contour
                rect = cv2.minAreaRect(c)
                #Drawing box around fount contour
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                #Drawing Red Box Around Contour
                cv2.drawContours(obj_stream,[box],0,(0,0,255),2)


                #Drawing number on contour
                cv2.putText(obj_stream, text, (cx, cy), font, 1, (0,255,0), 1, cv2.LINE_AA)

                #Find Height / Width for Distance Calculation
                width, height = rect[1]

                
                # Focal lenght = (Pixel Width x Distance) / Width
                # FL = (196 x 34in) / 13 in = 512.61

                # Distance = (Width x Focal Lenght) / Pixel Width
                distance = (13 * 512.61) / width

                #Adding Information to for console output
                console_Array.append([c_num, distance])
                
               
            cv2.imshow("Video", obj_stream)

            if computerVision.Enquiry(console_Array):
                UI.userInterface.object_Found(consoleBoxes, console_Array)
            else:
                UI.userInterface.object_NOT_Found(consoleBoxes)

            #Picture / Break if statement
            ch2 = cv2.waitKey(1)
            if ch2 & 0xFf == ord('q'):
                break

