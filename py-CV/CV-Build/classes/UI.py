import curses
import os
from colorclass import Color, Windows
from terminaltables import SingleTable
from colorclass import Color, Windows
from terminaltables import SingleTable

class userInteraction(object):

    Windows.enable(auto_colors=True, reset_atexit=True)
    begin_x = 35; begin_y = 0; height = 4; width = 30

    userConsole = '{autocyan}No{/autocyan}'
    userObject = '{autocyan}Pratice Square{/autocyan}'
    userCamera = '{autocyan}BUILT-IN{/autocyan}'

    def cls():
        os.system('cls' if os.name=='nt' else 'clear')


    def user_Camera(stdscr):
        print("What camera? (1 = USB, 0 = Built-in): ")
        userAnswer = stdscr.getch()

        if userAnswer == 49:
            userInteraction.userCamera = '{autocyan}USB{/autocyan}'
            print(1)
        else:
            userInteraction.userCamera = '{autocyan}BUILT-IN{/autocyan}'
            print(0)


    def user_Object(stdscr):
        print("What objct? 1 = Power Cube, 0 = Pratice Square")
        userAnswer = stdscr.getch()
  
        if userAnswer == 1:
            userInteraction.userObject = '{autocyan}Power Cube{/autocyan}'
            print(1)
        else:
            userInteraction.userObject = '{autocyan}Pratice Square{/autocyan}'
            print(0)


    def user_Console(stdscr):
        print("Enable Dynamic Console? 1 = Yes, 0 = No")
        userAnswer = stdscr.getch()

        if userAnswer == 1:
            userInteraction.userConsole = '{autocyan}Yes{/autocyan}'
            print(1)
        else:
            userInteraction.userConsole = '{autocyan}No{/autocyan}'
            print(0)

    def askCapture(stdscr):
        #Clears and resents
        stdscr.clear(); stdscr.refresh(); 
        #Turns on Keypad
        stdscr.keypad(True); curses.start_color()


        # Title Talbe
        cvTitle = SingleTable([['Computer Vision Program']])

        #User Choices
        choiceArray = [
            [Color('Camera'), Color(userInteraction.userCamera)],
            [Color('Target'), Color(userInteraction.userObject)],
            [Color('Console-Out'), Color(userInteraction.userConsole)]        
        ]

        userChoiceTable = SingleTable(choiceArray)
        userChoiceTable.inner_heading_row_border = False
        userChoiceTable.inner_row_border = True
        userChoiceTable.justify_columns = {0: 'center', 1: 'center', 2: 'center'}

        print(cvTitle.table)

        #Geting Operational Specifics
        userInteraction.user_Camera(stdscr)
        userInteraction.user_Object(stdscr)
        userInteraction.user_Console(stdscr)

        #Clear Screen
        userInteraction.cls()

        stdscr = curses.initscr()
        #Repriting Screen
        print(cvTitle.table)
        print(userChoiceTable.table)

      

        win_title = curses.newwin(userInteraction.height, userInteraction.width, userInteraction.begin_y, userInteraction.begin_x)
        win_title.box(0,0)

        win_title.refresh()

        counter = 0
  


        curses.endwin();