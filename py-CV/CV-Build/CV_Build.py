from classes import *
from curses import wrapper


def main():
   wrapper(userInteraction.askCapture)


#If Statement to call main function
if __name__ == '__main__':
    main()
