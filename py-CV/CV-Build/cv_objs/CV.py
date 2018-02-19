import numpy as np
import cv2
from cv_objs import UI

class computerVision(object):

    # Object Variable - for camera Choice and Console out options
    cube_user_inter = UI.userInterface()

    #To find if array is empty or not
    def Enquiry(self,lis1):
        if len(lis1) == 0:
            return False
        else:
            return True
   

    #Computer Vision Profile for Power-Cube
    def cubeProfile(stream, filtered_contours):

        #Adding Gauss Blur, - Number must be odd
        cube_blur  = cv2.GaussianBlur(stream, (21,21),0)
        #Converting picture to Hue, Saturation, Value Array
        hsv = cv2.cvtColor(cube_blur, cv2.COLOR_BGR2HSV)

        #Lower / Upper Limits for Color Selection
        lower_yellow = np.array([15,39,163])
        upper_yellow = np.array([25,139,233])

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

    
    #Main Vision-ID Method
    def comp_vision_start(self):

        

        stream = cv2.VideoCapture(0)
        
        while(True):

            #Array for storing filtered Contours / console array to send to console output
            filtered_contours = []
            console_Array = []

            #Contour Number for Identification
            c_num = 0

            _, obj_stream = stream.read()

            #Cube Profile return filtered_countours array
            computerVision.cubeProfile(obj_stream, filtered_contours)
          
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
                cv2.circle(obj_stream, (cx,cy), 4, (0, 0, 255), -1)

                #Area of Found Contour
                rect = cv2.minAreaRect(c)
                #Drawing box around fount contour
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                #Drawing Red Box Around Contour
                cv2.drawContours(obj_stream,[box],0,(0,0,255),2)


                #Drawing number on contour
                cv2.putText(obj_stream, text, (cx + 1, cy + 1), font, 1, (0,255,0), 1, cv2.LINE_AA)

                #Find Height / Width for Distance Calculation
                width, height = rect[1]

                
                # Focal length = (Pixel Width x Distance) / Width
                # FL = (196 x 34in) / 13 in = 512.61

                # Distance = (Width x Focal Length) / Pixel Width
                distance = (13 * 512.61) / width

                #Adding Information to for console output
                console_Array.append([c_num, distance, (cx, cy)])
                
            #drawing distance box
            self.cube_user_inter.draw_distance_Box(obj_stream)


            if self.Enquiry(console_Array) == True:
                self.cube_user_inter.draw_distance_number(console_Array, obj_stream)

                if self.cube_user_inter.check_cube_inRange_left(console_Array, obj_stream):
                    self.cube_user_inter.draw_grabber_lines_red_left(obj_stream)
                else:
                    self.cube_user_inter.draw_grabber_lines_green_left(obj_stream)

                if self.cube_user_inter.check_cube_inRange_right(console_Array, obj_stream):
                    self.cube_user_inter.draw_grabber_lines_red_right(obj_stream)
                else:
                    self.cube_user_inter.draw_grabber_lines_green_right(obj_stream)

            else:
                self.cube_user_inter.draw_grabber_lines_green_right(obj_stream)
                self.cube_user_inter.draw_grabber_lines_green_left(obj_stream)

            

            #displaying video
            cv2.imshow("Cube_Vid", obj_stream)

            ch2 = cv2.waitKey(1)
            if ch2 & 0xFf == ord('q'):
                break

