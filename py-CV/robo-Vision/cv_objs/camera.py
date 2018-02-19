import cv2
from cv_objs import *

class VideoCamera(object):
    #Member Objects
    cv_vid = computerVision()

    def __init__(self):
        #starts video Capture
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        #Grabs frame
        success, obj_stream = self.video.read()

        #Processes Image
        obj_stream = self.cv_vid.comp_vision_start(obj_stream)

        #Returns it as .jpeg
        ret, jpeg = cv2.imencode('.jpg', obj_stream)
        return jpeg.tobytes()