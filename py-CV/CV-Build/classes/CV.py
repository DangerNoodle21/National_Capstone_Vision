import numpy as np
import cv2
import terminaltables


class computerVision(object):

    def vid_stream(userChoice):

        #Starts Video Stream From User Choice
        stream = cv2.videoCapture(userCHoice)
        
        while(True):

            #Capturing Video Frame-by-Frame
            ret, v_cap = stream.read()

            video_stream_gray = cv2.cvtColor(video_stream, cv2.COLOR_RGB2GRAY)

            frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)
            cv2.imshow("Video", frame)


            #Picture / Break if statement
            ch2 = cv2.waitKey(1)
            if ch2 & 0xFF == ord('p'):
                keyboard()
            elif ch2 & 0xFf == ord('q'):
                break


