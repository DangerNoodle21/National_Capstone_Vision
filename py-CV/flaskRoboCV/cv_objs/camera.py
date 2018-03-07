import cv2
import imutils
from cv_objs import *

class VideoCamera(object):
    #Member Objects
    

    def __init__(self):
        #starts video Capture
        vs = CAM_STREAM.CAM_STREAM(0)
        compVision = CV.computerVision(1)
        i2c_obj = I2C.I2C(0x04)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        #Grabs frame
        success, vid_stream = self.vs.read()

        console_Array, processed_vid = compVision.comp_vision_start(vid_stream)

        user_Inter.draw_UI_elements(console_Array, processed_vid)

        vid_stream = imutils.resize(vid_stream, width=400)

        i2c_obj.send_I2C_data(console_Array)
       
        #Returns it as .jpeg
        ret, jpeg = cv2.imencode('.jpg', vid_stream)
        return jpeg.tobytes()