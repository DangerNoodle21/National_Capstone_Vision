import numpy as np
import cv2
import argparse
from cv_objs import *

class computerVision:

    # Object Variable - for camera Choice and Console out options
    target_Choice = 0

    def __init__(self, choice):
        self.target_Choice = choice

    #Computer Vision Profile for Power-Cube
    def cubeProfile(self, stream, filtered_contours):

        #Adding Gauss Blur, - Number must be odd
        cube_blur  = cv2.GaussianBlur(stream, (21,21),0)
        #Converting picture to Hue, Saturation, Value Array
        hsv = cv2.cvtColor(cube_blur, cv2.COLOR_BGR2HSV)

        #Lower / Upper Limits for Color Selection
        lower_yellow = np.array([24,28,92])
        upper_yellow = np.array([45,138,252])

        #Removing Everything but the desired color
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
          
        #returns an Arrays "Contours"
        _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Compare Value to Eliminate Duplicate Contours
        compare_value = 0
        
        #Filtering For Loop for Contours based up aspect-ratio of cube - Aspect Ratio : 0.80139

        for c in contours:

            #Calculating Minimum Rectangle for contour
            rect_filter = cv2.minAreaRect(c)

            #Determining Width / Height of box
            width_filter, height_filter = rect_filter[1]

            #to Avoid Division by Zeros errors
            if height_filter == 0: 
                continue
            #If distance is over 1000 inches, skip
            if (13 * 512.61) / width_filter > 600: 
                continue
            #Aspect Ratio Filter, Above & equal to 1, skip
            elif width_filter  / height_filter >= 1: 
                continue
            elif width_filter  / height_filter < 0.5: 
                continue
            #Avoiding duplicate contours
            elif width_filter  / height_filter == compare_value: 
                continue
            else: 
               compare_value  = width_filter/height_filter
               filtered_contours.append(c)

            return filtered_contours

    
    #Main Computer-Vision Method
    def comp_vision_start(self, vid_stream):

        #Array for storing filtered Contours / console array to send to console output
        filtered_contours = []
        console_Array = []

        #Contour Number for Identification
        c_num = 0

        if self.target_Choice > 0:
            self.cubeProfile(vid_stream, filtered_contours)

          
        #Number of Filtered Contours
        con_filtered = len(filtered_contours)
        #Array for drawing contours
        objects = np.zeros([vid_stream.shape[0], vid_stream.shape[1],3], 'uint8')

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
            cv2.circle(vid_stream, (cx,cy), 4, (0, 0, 255), -1)

            #Area of Found Contour
            rect = cv2.minAreaRect(c)
            #Drawing box around fount contour
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            #Drawing Red Box Around Contour
            cv2.drawContours(vid_stream,[box],0,(0,0,255),2)


            #Drawing number on contour
            cv2.putText(vid_stream, text, (cx + 1, cy + 1), font, 1, (0,255,0), 1, cv2.LINE_AA)

            #Find Height / Width for Distance Calculation
            width, height = rect[1]

                
            # Focal length = (Pixel Width x Distance) / Width
            # FL = (196 x 34in) / 13 in = 512.61

            # Distance = (Width x Focal Length) / Pixel Width
            distance = (13 * 512.61) / width

            #Adding Information to for console output
            console_Array.append([c_num, distance, (cx, cy)])
                
       

        return console_Array, vid_stream