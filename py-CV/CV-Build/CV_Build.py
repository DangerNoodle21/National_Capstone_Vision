from classes import *
from curses import wrapper


#globe viables
cameraChoice = 0

def main():
    #cameraChoice = userInteraction.askCapture()
    cameraChoice = 0
    wrapper(computerVision.vid_stream, cameraChoice)




#If Statement to call main function
if __name__ == '__main__':
    main()
