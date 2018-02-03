
import cv2
import numpy as np

class class1(object):

    userChoice = ""

    def askCapture():
        userChoice = input("Webcam? 0 = no, 1 = yes")

        if userChoice == "1":
            video_cap = cv2.VideoCapture(1)
        else:
            video_cap = cv2.VideoCapture(0)

        return video_cap;



