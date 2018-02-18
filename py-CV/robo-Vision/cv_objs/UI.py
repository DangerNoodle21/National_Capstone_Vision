import cv2
import numpy as np

class userInterface(object):
    #getting video out information
    line_type = cv2.LINE_AA
    line_thinkness = 3
    green_color = (0, 255, 0)
    red_color = (0,0,255)


    def draw_distance_Box(self, vid_stream):
        height, width = vid_stream.shape[0:2]
        rec_multiplyer = 40

        #S_L_Y = Start Left X Coordinate / S_R_Y = Start Right X Coordinate
        s_x = int((width / 2) - rec_multiplyer)
        s_y = rec_multiplyer

        #S_L_Y = end right Y Coordinate / S_R_Y = Start Right Y Coordinate
        e_y = rec_multiplyer + rec_multiplyer
        e_x = int((width / 2) + rec_multiplyer)

        cv2.rectangle(vid_stream, (s_x, s_y),(e_x, e_y), self.green_color, self.line_thinkness)



    def set_xy_grabber_lines(self, vid_stream):
        height, width = vid_stream.shape[0:2]
        #S_L_Y = Start Left X Coordinate / S_R_Y = Start Right X Coordinate
        s_l_x = 10
        s_r_x = width - 10

        #S_L_Y = Start Left Y Coordinate / S_R_Y = Start Right Y Coordinate
        s_l_y = int(height - ( height  / 3 ))
        s_r_y = s_l_y

        #E_L_Y = End Left X Coordinate / E_R_Y = End Right X Coordinate
        e_l_x = int((width /2) - 20)
        e_r_x = int((width /2) + 20)

        #E_L_Y = End Left Y Coordinate / E_R_Y = End Right Y Coordinate
        e_l_y = height - 10
        e_r_y = e_l_y

        return (s_l_x, s_l_y), (e_l_x, e_l_y), (s_r_x, s_r_y), (e_r_x, e_r_y) 


    def draw_grabber_lines_green(self, vid_stream_green):
        
        #getting line coordinates
        coordinates = self.set_xy_grabber_lines(vid_stream_green)

        #Drawing left grabber line
        s_l_x, s_l_y  = coordinates[0]
        e_l_x, e_l_y = coordinates[1]

        cv2.line(vid_stream_green, (s_l_x, s_l_y), (e_l_x, e_l_y), self.green_color, self.line_thinkness)

        #Drawing left grabber line
        s_r_x, s_r_y  = coordinates[2]
        e_r_x, e_r_y = coordinates[3]

        cv2.line(vid_stream_green, (s_r_x, s_r_y), (e_r_x, e_r_y), self.green_color, self.line_thinkness)

    def draw_grabber_lines_red(self, vid_stream_red):
        
        #getting line coordinates
        coordinates = userInterface.set_xy_grabber_lines(vid_stream_green)

        #Drawing left grabber line
        s_l_x, s_l_y  = coordinates[0]
        e_l_x, e_l_y = coordinates[1]

        cv2.line(vid_stream_red, (s_l_x, s_l_y), (e_l_x, e_l_y), self.red_color, self.line_thinkness)

        #Drawing left grabber line
        s_r_x, s_r_y  = coordinates[2]
        e_r_x, e_r_y = coordinates[3]

        cv2.line(vid_stream_red, (s_r_x, s_r_y), (e_r_x, e_r_y), self.red_color, self.line_thinkness)