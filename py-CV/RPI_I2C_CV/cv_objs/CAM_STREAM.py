from threading import Thread
import cv2

class CAM_STREAM:

    def __init__(self, src=0):
        #Initialize the video stream with source of 0
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False


    def start(self):
        Thread(target = self.update, args=()).start()
        return self

    def update(self):
        #Keep looping until the thread is stopped
        while True:
            #if the thread indicator is stopped, stop the 
            if self.stopped:
                return

            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
