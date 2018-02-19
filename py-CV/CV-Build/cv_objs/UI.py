import cv2
import numpy as np

class userInterface(object):


    #Object Variables

    line_type = cv2.LINE_AA
    line_thinkness_rectangle = 3
    line_thinkness_grabbers= 5
    green_color = (0, 255, 0)
    red_color = (0,0,255)
    rectangle_multiplyer = 40
    font = cv2.FONT_HERSHEY_SIMPLEX



    def check_cube_inRange_left(self, array, vid_stream):
        c_num, distance, (cx, cy) = array[0]
        
        coordinates = self.get_xy_grabber_lines(vid_stream)
        e_l_x, e_l_y  = coordinates[1]

        if cx <= e_l_x:
            return True
        else:
            return False

    def check_cube_inRange_right(self, array, vid_stream):
        c_num, distance, (cx, cy) = array[0]
        
        coordinates = self.get_xy_grabber_lines(vid_stream)
        e_r_x, e_r_y  = coordinates[2]

        if cx >= e_r_x:
            return True
        else:
            return False

    def get_xy_grabber_lines(self, vid_stream):
        height, width = vid_stream.shape[0:2]

        start_x_mulit = 20
        end_x_mulit = 40

        #S_L_Y = Start Left X Coordinate / S_R_Y = Start Right X Coordinate
        s_l_x = start_x_mulit
        s_r_x = width - start_x_mulit

        #S_L_Y = Start Left Y Coordinate / S_R_Y = Start Right Y Coordinate
        s_l_y = int(height - ( height  / 3 ))
        s_r_y = s_l_y

        #E_L_Y = End Left X Coordinate / E_R_Y = End Right X Coordinate
        e_l_x = int((width /2) - end_x_mulit)
        e_r_x = int((width /2) + end_x_mulit)

        #E_L_Y = End Left Y Coordinate / E_R_Y = End Right Y Coordinate
        e_l_y = height - 10
        e_r_y = e_l_y

        return (s_l_x, s_l_y), (e_l_x, e_l_y), (s_r_x, s_r_y), (e_r_x, e_r_y)

    def draw_distance_Box(self, vid_stream):
        height, width = vid_stream.shape[0:2]
        
        #S_L_Y = Start Left X Coordinate / S_R_Y = Start Right X Coordinate
        s_x = int((width / 2) - (1.5 *self.rectangle_multiplyer))
        s_y = self.rectangle_multiplyer

        #S_L_Y = end right Y Coordinate / S_R_Y = Start Right Y Coordinate
        e_y = 2 * self.rectangle_multiplyer
        e_x = int((width / 2) + (1.5 *self.rectangle_multiplyer))

        cv2.rectangle(vid_stream, (s_x, s_y),(e_x, e_y), self.green_color, self.line_thinkness_rectangle)

    def draw_distance_number(self, array, vid_stream):
        c_num, distance, (cx, cy) = array[0]
        height, width = vid_stream.shape[0:2]

        distance = str(int(distance))

        #S_L_Y = Start Left X Coordinate / S_R_Y = Start Right X Coordinate
        s_x = int((width / 2) - 15)
        s_y = self.rectangle_multiplyer + 32


        cv2.putText(vid_stream, distance, (s_x, s_y), self.font, 1, self.green_color, 1, cv2.LINE_AA)



    def draw_grabber_lines_green_left(self, vid_stream):
        
        #getting line coordinates
        coordinates = self.get_xy_grabber_lines(vid_stream)

        #Drawing left grabber line
        s_l_x, s_l_y  = coordinates[0]
        e_l_x, e_l_y = coordinates[1]

        cv2.line(vid_stream, (s_l_x, s_l_y), (e_l_x, e_l_y), self.green_color, self.line_thinkness_grabbers)

    def draw_grabber_lines_green_right(self, vid_stream):
        
        #getting line coordinates
        coordinates = self.get_xy_grabber_lines(vid_stream)

        #Drawing left grabber line
        s_r_x, s_r_y  = coordinates[2]
        e_r_x, e_r_y = coordinates[3]

        cv2.line(vid_stream, (s_r_x, s_r_y), (e_r_x, e_r_y), self.green_color, self.line_thinkness_grabbers)

   
   
    def draw_grabber_lines_red_left(self, vid_stream):
        
        #getting line coordinates
        coordinates = self.get_xy_grabber_lines(vid_stream)

        #Drawing left grabber line
        s_l_x, s_l_y  = coordinates[0]
        e_l_x, e_l_y = coordinates[1]

        cv2.line(vid_stream, (s_l_x, s_l_y), (e_l_x, e_l_y), self.red_color, self.line_thinkness_grabbers)

    def draw_grabber_lines_red_right(self, vid_stream):
        
        #getting line coordinates
        coordinates = self.get_xy_grabber_lines(vid_stream)

        #Drawing left grabber line
        s_l_x, s_l_y  = coordinates[0]
        e_l_x, e_l_y = coordinates[1]

        cv2.line(vid_stream, (s_l_x, s_l_y), (e_l_x, e_l_y), self.red_color, self.line_thinkness_grabbers)