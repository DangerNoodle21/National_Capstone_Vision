import numpy as np
import cv2
import terminaltables
import curses

class computerVision(object):

    #To find if array is empty or not
    def Enquiry(lis1):
        if len(lis1) == 0:
            return False
        else:
            return True


    def cusreBoxCreator():

        curses.start_color(); curses.curs_set(False);

        #User Information Box Settings
        userBox_x_height = 5; userBox_width = 10; userBox_y = 0;  userBox_x = 0; 

        #Distance Dispaly boxes Settings
        disWin_height = 5; disWin_width = 10; disWin_y = 0;  disWin_x = 12; 

        #Curses Window Creation [curses.newwin(nlines, ncols, begin_y, begin_x)]
        idWindow_1 = curses.newwin(userBox_x_height, userBox_width, userBox_y, userBox_x); idWindow_1.box(0,0); 
        idWindow_2 = curses.newwin(userBox_x_height, userBox_width, userBox_y + 6, userBox_x); idWindow_2.box(0,0); 
        idWindow_3 = curses.newwin(userBox_x_height, userBox_width, userBox_y + 12, userBox_x); idWindow_3.box(0,0);

        #idWindow_1.wmove(userBox_y + 2, userBox_x + 2)
        idWindow_1.addstr("USB CAM")
        idWindow_1.refresh()

        #idWindow_2.wmove(userBox_y + 8, userBox_x + 2)
        idWindow_2.addstr("TARGET SQUARE")
        idWindow_2.refresh()

        #idWindow_3.wmove(userBox_y + 14, userBox_x + 2)
        idWindow_3.addstr("CONSOLE")
        idWindow_3.refresh()



        
        dis_Window_title = curses.newwin(disWin_height, disWin_width, disWin_y, disWin_x); dis_Window_title.box(0,0); 
        dis_Window_info = curses.newwin(disWin_height + 10, disWin_width, disWin_y + 6, disWin_x); dis_Window_info.box(0,0); 
    
        
        #dis_Window_title.wmove(disWin_y + 2, disWin_x + 2)
        dis_Window_title.addstr("NOT FOUND")
        dis_Window_title.refresh()
        dis_Window_info.refresh()
        
        
        return {'idWindow_1': idWindow_1, 'idWindow_2':idWindow_2, 'idWindow_3':idWindow_3, 
                'dis_Window_title':dis_Window_title, 'dis_Window_info':dis_Window_info}


    def vid_stream(stdscr, userChoice):




        boxes = computerVision.cusreBoxCreator()
     

        stream = cv2.VideoCapture(0)
        
        while(True):

            #Array for storing flitered Contours / console array to send to console output
            filtered = []
            console_Array = []

            #Contour Number for Identifaction
            c_num = 0

            #Pulls image from stream
            ret, video_stream = stream.read()

            # Converts to gray scale / Adds Blur / Converst to CannyEdge Detection
            video_stream_gray = cv2.cvtColor(video_stream, cv2.COLOR_RGB2GRAY)
            video_stream_gray = cv2.GaussianBlur(video_stream_gray, (3,3),0)
            video_stream_gray = cv2.Canny(video_stream_gray, 50, 200, None, 3)


            #Finds the Contours in frame taken, then prints the amount it finds
            _, contours, hierarchy = cv2.findContours(video_stream_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            con_unFiltered = len(contours)

            #For loop for filtering out contours based on pixel Area
            for c in contours:
                rect = cv2.minAreaRect(c)
                width_filter, height_filter = rect[1]
                if height_filter == 0:
                    continue
                elif width_filter/height_filter > 1.41:
                    continue
                elif width_filter/height_filter < 1.40:
                    continue
                else:
                    filtered.append(c)

            #Number of Filtered Contours
            con_filtered = len(filtered)
            #Array for drawing contours
            objects = np.zeros([video_stream.shape[0], video_stream.shape[1],3], 'uint8')

            #For Loop for Filtering Contours - C the number of filtered countours in the array Filtered[]
            for c in filtered:

                #Contour Number
                c_num = c_num + 1
                font = cv2.FONT_HERSHEY_SIMPLEX
                text = str(c_num)

                #Centriod
                # Had to add +1 to advoid Dividion by Zero erro
                M = cv2.moments(c)
                cx = int( M['m10']/(M['m00'] + 1))
                cy = int( M['m01']/(M['m00'] + 1))

                #Centriods
                cv2.circle(objects, (cx,cy), 4, (0, 0, 255), -1)

                #Area of Found Contour
                rect = cv2.minAreaRect(c)
                #Drawing box around fount contour
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                #Drawing Red Box Around Contour
                cv2.drawContours(video_stream,[box],0,(0,0,255),2)


                #Drawing number on contour
                cv2.putText(video_stream, text, (cx, cy), font, 1, (0,255,0), 1, cv2.LINE_AA)

                #Find Height / Width for Distance Calculation
                width, height = rect[1]
                distance = (3*639.9) / width
                #Adding Information to for console output
                console_Array.append([c_num, width/height, distance])
               
            cv2.imshow("Video", video_stream)

            if computerVision.Enquiry(console_Array):
                boxes['dis_Window_title'].erase()
    
                boxes['dis_Window_title'].addstr("Found")
                boxes['dis_Window_title'].box(0,0); 
                boxes['dis_Window_title'].refresh()
            else:
                boxes['dis_Window_title'].erase()
                boxes['dis_Window_title'].box(0,0); 
                boxes['dis_Window_title'].addstr("Not Found")
                boxes['dis_Window_title'].refresh()

            #Picture / Break if statement
            ch2 = cv2.waitKey(1)
            if ch2 & 0xFf == ord('q'):
                break

