import curses


class userInteraction(object):

    def user_Camera(stdscr):
        print("What camera? 1 = USB, 0 = Built-in")
        userAnswer = stdscr.getch()
        if userAnswer == 49:
            userCamera = '{autocyan}USB{/autocyan}'
        else:
            userCamera = '{autocyan}BUILT-IN{/autocyan}'

        return userCamera


    def user_Object(stdscr):
        print("What objct? 1 = Power Cube, 0 = Pratice Square")
        userAnswer = stdscr.getch()
        if userAnswer == 49:
            userObject = '{autocyan}Power Cube{/autocyan}'
        else:
            userObject = '{autocyan}Pratice Square{/autocyan}'


    def user_Console(stdscr):
        print("Enable Dynamic Console? 1 = Yes, 0 = No")
        userAnswer = stdscr.getch()
        if userAnswer == 49:
            userConsole = '{autocyan}Yes{/autocyan}'
        else:
            userConsole = '{autocyan}No{/autocyan}'

    def askCapture(stdscr):

        stdscr = curses.initscr()

        stdscr.clear()
        stdscr.refresh()
        
        stdscr.keypad(True)
        curses.start_color()

 
        begin_x = 20; begin_y = 7; height = 5; width = 40

        win_title = curses.newwin(height, width, begin_y, begin_x)
        win_title.box(0,0)



        stdscr.refresh()
        win_title.refresh()

        counter = 0
  


        curses.endwin();