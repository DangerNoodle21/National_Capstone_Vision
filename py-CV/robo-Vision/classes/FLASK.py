from flask import Flask, render_template, Response
import cv2
import numpy

class FLASK(object):

    def get_frame(vid_stream):


        success, image = vid_stream.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()