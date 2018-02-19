from cv_objs import CV
import numpy as np
import cv2

def main():

    vid_choice = 0
    console_out = 0
    cube_id_stream_1 = CV.computerVision(vid_choice, console_out)
    cube_id_stream_1.comp_vision_start()



#If Statement to call main function
if __name__ == '__main__':
    main()
