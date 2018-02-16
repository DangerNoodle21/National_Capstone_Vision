import curses
import cv2


class userInterface(object):


    
    def draw_menu(stdscr):
        k = 0
        cursor_x = 0
        cursor_y = 0

        stdscr.clear()
        stdscr.refresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # Loop where k is the last character pressed
        while (k == 0):

            # Initialization
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            if k == curses.KEY_DOWN:
                cursor_y = cursor_y + 1
            elif k == curses.KEY_UP:
                cursor_y = cursor_y - 1
            elif k == curses.KEY_RIGHT:
                cursor_x = cursor_x + 1
            elif k == curses.KEY_LEFT:
                cursor_x = cursor_x - 1

            cursor_x = max(0, cursor_x)
            cursor_x = min(width-1, cursor_x)

            cursor_y = max(0, cursor_y)
            cursor_y = min(height-1, cursor_y)

            # Declaration of strings
            title = "Computer Vision with Python"[:width-1]
            subtitle = "By Marc Lewis"[:width-1]
            keystr = "Press any key to continue"[:width-1]
            statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
            if k == 0:
                keystr = "Press any key to continue..."[:width-1]

            # Centering calculations
            start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
            start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
            start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
            start_y = int((height // 2) - 2)

            # Rendering some text
            whstr = "Width: {}, Height: {}".format(width, height)
            stdscr.addstr(0, 0, whstr, curses.color_pair(1))

            # Render status bar
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(height-1, 0, statusbarstr)
            stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
            stdscr.attroff(curses.color_pair(3))

            # Turning on attributes for title
            stdscr.attron(curses.color_pair(2))
            stdscr.attron(curses.A_BOLD)

            # Rendering title
            stdscr.addstr(start_y, start_x_title, title)

            # Turning off attributes for title
            stdscr.attroff(curses.color_pair(2))
            stdscr.attroff(curses.A_BOLD)

            # Print rest of text
            stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
            stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
            stdscr.addstr(start_y + 5, start_x_keystr, keystr)
            stdscr.move(cursor_y, cursor_x)

            # Refresh the screen
            stdscr.refresh()

            # Wait for next input
            k = stdscr.getch()


    def outputBoxCreator(stdscr):

        stdscr.clear(); stdscr.refresh()

        #Curses Color Pairs - For Found / Not-Found
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        #User Information Box Settings
        userBox_x_height = 5; userBox_width = 20; userBox_y = 0;  userBox_x = 0; 

        #Distance Display boxes Settings
        disWin_height = 5; disWin_width = 20; disWin_y = 0;  disWin_x = userBox_width + 2; 

        #Curses Window Creation - User Choices
        #[curses.newwin(nlines, ncols, begin_y, begin_x)]
        userWindow_1 = curses.newwin(userBox_x_height, userBox_width, userBox_y, userBox_x); userWindow_1.box(0,0); 
        userWindow_2 = curses.newwin(userBox_x_height, userBox_width, userBox_y + 6, userBox_x); userWindow_2.box(0,0); 
        userWindow_3 = curses.newwin(userBox_x_height, userBox_width, userBox_y + 12, userBox_x); userWindow_3.box(0,0);
        
        #Adding Words Windows
        userWindow_1.addstr(2, 2, "USB CAM", curses.COLOR_RED)
        userWindow_2.addstr(2, 2, "Power-Cube")
        userWindow_3.addstr(2, 2, "CONSOLE Enabled")

        #Refreshing the Windows
        userWindow_1.refresh(); userWindow_2.refresh(); userWindow_3.refresh();

        #Creating New Windows - Distance Display
        dis_Window_title = curses.newwin(disWin_height, disWin_width, disWin_y, disWin_x); dis_Window_title.box(0,0); 
        dis_Window_info = curses.newwin(disWin_height + 10, disWin_width, disWin_y + 6, disWin_x); dis_Window_info.box(0,0);

        #Adding Words to the windows
        dis_Window_title.attron(curses.color_pair(1))
        dis_Window_title.attron(curses.A_BOLD)
        dis_Window_title.addstr(2,2,"NOT FOUND")
        

        #Refreshing the Windows
        dis_Window_title.refresh(); dis_Window_info.refresh();
        
        
        return {'userWindow_1': userWindow_1, 'userWindow_2':userWindow_2, 'userWindow_3':userWindow_3, 
                'dis_Window_title':dis_Window_title, 'dis_Window_info':dis_Window_info}

    def object_Found(consoleBoxes):

        consoleBoxes['dis_Window_title'].erase()

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        

        consoleBoxes['dis_Window_title'].attron(curses.color_pair(1))
        consoleBoxes['dis_Window_title'].attron(curses.A_BOLD)


       
        consoleBoxes['dis_Window_title'].addstr(2,2,"OBJ. DETECTED")
        consoleBoxes['dis_Window_title'].box(0,0); 
        consoleBoxes['dis_Window_title'].refresh()

    def object_NOT_Found(consoleBoxes):


        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


        consoleBoxes['dis_Window_title'].erase()
        nsoleBoxes['dis_Window_title'].attron(curses.color_pair(1))
        consoleBoxes['dis_Window_title'].attron(curses.A_BOLD)


        consoleBoxes['dis_Window_title'].addstr(2,2,"NO OBJ.")
        consoleBoxes['dis_Window_title'].box(0,0); 
        consoleBoxes['dis_Window_title'].refresh()