from flask import Flask, render_template, Response
import cv2
import numpy

class FLASK(object):

    app = Flask(__name__)


    def get_frame(vid_stream):
        success, image = vid_stream.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


    @app.route('/')
    def index():
        return render_template('index.html')

    def gen(camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


    @app.route('/video_feed')
    def video_feed():
        return Response(gen(VideoCamera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


   