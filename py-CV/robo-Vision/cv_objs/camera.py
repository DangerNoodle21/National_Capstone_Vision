import cv2
from cv_objs import *

class VideoCamera(object):
    cv_vid = computerVision()
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, obj_stream = self.video.read()

        obj_stream = self.cv_vid.comp_vision_start(obj_stream)


        ret, jpeg = cv2.imencode('.jpg', obj_stream)
        return jpeg.tobytes()