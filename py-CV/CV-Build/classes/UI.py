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



    def user_Camera():
        userAnswer = input("What camera? (1 = USB, 0 = Built-in): ")
        print(userAnswer)

        if userAnswer == 1:
            userInteraction.userCamera = '{autocyan}USB{/autocyan}'

        else:
            userInteraction.userCamera = '{autocyan}BUILT-IN{/autocyan}'
        return userAnswer



    def user_Object():
        userAnswer = input("What objct? 1 = Power Cube, 0 = Pratice Square")
        print(userAnswer)
        if userAnswer == 1:
            userInteraction.userObject = '{autocyan}Power Cube{/autocyan}'
        else:
            userInteraction.userObject = '{autocyan}Pratice Square{/autocyan}'


    def user_Console():
        userAnswer = input("Enable Dynamic Console? 1 = Yes, 0 = No")
        print(userAnswer)
        if userAnswer == 1:
            userInteraction.userConsole = '{autocyan}Yes{/autocyan}'
            
        else:
            userInteraction.userConsole = '{autocyan}No{/autocyan}'

    
    def askCapture():

        # Title Talbe
        cvTitle = SingleTable([['Computer Vision Program']])

        #User Choices
        choiceArray = [
            [Color('Camera'), Color(userInteraction.userCamera)],
            [Color('Target'), Color(userInteraction.userObject)],
            [Color('Console-Out'), Color(userInteraction.userConsole)]        
        ]

        #User Table Creation
        userChoiceTable = SingleTable(choiceArray)
        #Table Formatting
        userChoiceTable.inner_heading_row_border = False
        userChoiceTable.inner_row_border = True
        userChoiceTable.justify_columns = {0: 'center', 1: 'center', 2: 'center'}

        

        #Getting User Options
        camera = userInteraction.user_Camera()
        userInteraction.user_Object()
        userInteraction.user_Console()

        #Clears Screen
        userInteraction.cls()
      
        return camera