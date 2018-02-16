from classes import *
from curses import wrapper


def main():
    wrapper(userInterface.draw_menu)


    wrapper(computerVision.comp_vision_start)


#If Statement to call main function
if __name__ == '__main__':
    main()
