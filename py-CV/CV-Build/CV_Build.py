from classes import *
from curses import wrapper


def main():

    vid1 = computerVision(0, 1)

    wrapper(vid1.comp_vision_start())


#If Statement to call main function
if __name__ == '__main__':
    main()
