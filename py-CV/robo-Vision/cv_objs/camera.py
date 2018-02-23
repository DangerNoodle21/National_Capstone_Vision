import cv2
from cv_objs import *

class VideoCamera(object):
    #Member Objects
    cv_vid = computerVision(1, 0x04)

    def __init__(self):
        #starts video Capture
        vs = WebcamVideoStream(src=0).start()

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        #Grabs frame
        success, vid_stream = self.vs.read()
        vid_stream = imutils.resize(vid_stream, width=400)

        #Processes Image
        vid_stream = self.cv_vid.comp_vision_start(vid_stream)

        #Returns it as .jpeg
        ret, jpeg = cv2.imencode('.jpg', obj_stream)
        return jpeg.tobytes()