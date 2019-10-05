import numpy as np
import random
import time

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(0)

#don't change the class name
class AI(object):


    #chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
    #    global turn_color
        self.chessboard_size = chessboard_size

        #You are white or black
        self.color = color

        #the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
        self.candidate_list = []

    # The input is current chessboard.
    def go(self, chessboard):
        for i in range(0,14):
            print(' ')
            for j in range(0,14):

                if chessboard[i,j]==-1:
                    print(2, end='')
                    print(' ,', end='')
                elif chessboard[i,j]==1 :
                    print(1, end='')
                    print(' ,', end='')
                else:
                    print(0, end='')
                    print(' ,', end='')
        print(' ')
        # Clear candidate_list
        self.candidate_list.clear()
        #上下左右

        #==================================================================
        #Write your algorithm here、
        #Here is the simplest sample:Random decision

        #idx = np.where(chessboard == COLOR_NONE)

       # idx = list(zip(idx[0], idx[1]))
       # pos_idx = random.randint(0, len(idx)-1)
        new_pos = [0,0]

        list1 = self.the_max_grades( self.color, chessboard)
       # print(232131242412412)
        list2 = self.the_max_grades( -self.color, chessboard)
        print(list1)
        print(list2)
        print(self.color)
       # print('asdasd')

        #  print(list2)
        #if list1[0]>=100000 or list2[0]>=100000

        if list1[0]>=list2[0]:

            new_pos[0] = list1[1][0]
            new_pos[1] = list1[1][1]
        else :

            new_pos[0] = list2[1][0]
            new_pos[1] = list2[1][1]



        if    chessboard[5,5]==COLOR_NONE and list1[0]== and list2[0]==4:
            new_pos[0]=5
            new_pos[1]=5





        #==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        #If not, return error.
       # assert chessboard[new_pos[0],new_pos[1]]== COLOR_NONE
        #Add your decision into candidate_list, Records the chess board
        self.candidate_list.append(new_pos)

    def count_continue(self, color, main, last, chessboard, direction):
        center_left =[0,0]
        center_right = [0,0]
        main_plus =0
        last_plus =0
        if direction =='vertical':
            main_plus=-1

        elif direction =='cross':
            last_plus= 1

        elif direction =='right':
            main_plus = 1
            last_plus = -1

        else :
            main_plus = 1
            last_plus = 1

        center_left[0] = main - main_plus
        center_left[1] = last - last_plus
        center_right[0] = main +main_plus
        center_right[1] = last + last_plus

        count = 1
        temp_main = main+main_plus
        temp_last = last+last_plus
        if temp_main<=14 and temp_main>=0 and temp_last<=14 and temp_last>=0:
            while chessboard[ temp_main, temp_last] ==color :

                count+=1

                temp_main=temp_main+main_plus
                temp_last=temp_last+last_plus

                center_right[0] = temp_main
                center_right[1] = temp_last
                if not (temp_main <= 14 and temp_main >= 0 and temp_last <= 14 and temp_last >= 0):
                    break
               # print(count)
               # print(center_right)
               # print(chessboard[center_right[0], center_right[1]])
                #print('----------')


        temp_main=main-main_plus
        temp_last=last-last_plus

        if  temp_main<=14 and temp_main>=0 and temp_last<=14 and temp_last>=0:
            while chessboard[ temp_main, temp_last] ==color:
                count+=1

                temp_main=temp_main-main_plus
                temp_last=temp_last-last_plus

                center_left[0] = temp_main
                center_left[1] = temp_last
                if not (temp_main <= 14 and temp_main >= 0 and temp_last <= 14 and temp_last >= 0):
                    break
               # print(count)



        return count, center_left, center_right, main_plus, last_plus

    def count_grades(self, color, x, y, chessboard, direction):


        list = self.count_continue(color =color, main = x, last = y,chessboard=chessboard, direction=direction)
        cont = list[0]

        left_point = list[1]
        right_point = list[2]
        x_plus = list[3]
        y_plus = list[4]

        if cont >= 5 :
            return 'win_5'
        elif cont==4:#没考虑边界
            if(self.the_color(chessboard, left_point,color)==COLOR_NONE and self.the_color(chessboard, right_point,color)==COLOR_NONE):
                return 'live_4'
            elif (self.the_color(chessboard, left_point,color)==color and self.the_color(chessboard, right_point,color)==color):
                return 'nothing'
            elif (self.the_color(chessboard, left_point,color)==COLOR_NONE or self.the_color(chessboard, right_point,color)==COLOR_NONE):
                return 'die_4'
        elif cont==3 :
            left_left_point = [0,0]
            right_right_point = [0, 0]

            left_left_point[0] = left_point[0]-x_plus
            left_left_point[1] = left_point[1] - y_plus
            right_right_point[0]=right_point[0]+x_plus
            right_right_point[1]=right_point[1]+y_plus
            if (self.the_color(chessboard, left_point,color) == COLOR_NONE and self.the_color(chessboard, right_point,color)== COLOR_NONE):
                if self.the_color(chessboard, left_left_point, color)==-color and self.the_color(chessboard, right_right_point,color)==-color:
                    return 'die_3'
                elif self.the_color(chessboard, left_left_point, color)==color or self.the_color(chessboard, right_right_point, color)== color:
                    return 'low_die_4'
                elif self.the_color(chessboard, left_left_point, color) == COLOR_NONE or self.the_color(chessboard,  right_right_point, color) == COLOR_NONE:
                    return 'live_3'

            elif self.the_color(chessboard, left_point, color) == -color and self.the_color(chessboard,  right_point, color) == -color:
                return 'nothing'
            elif self.the_color(chessboard, left_point, color) == COLOR_NONE or self.the_color(chessboard,  right_point, color) == COLOR_NONE:
                if self.the_color(chessboard, left_point, color)==-color:
                    if(self.the_color(chessboard, right_right_point, color)==-color):
                        return 'nothing'
                    elif (self.the_color(chessboard, right_right_point, color)==COLOR_NONE):
                        return 'die_3'
                    if self.the_color(chessboard, right_right_point, color)==color:
                        return 'low_die_4'

                if self.the_color(chessboard, right_point, color)==-color:
                    if(self.the_color(chessboard, left_left_point, color)==-color):
                        return 'nothing'
                    elif (self.the_color(chessboard, left_left_point, color)==COLOR_NONE):
                        return 'die_3'
                    if self.the_color(chessboard, left_left_point, color)==color:
                        print('l4')
                        return 'low_die_4'

        elif cont ==2:
            left_left_point = [0, 0]
            right_right_point = [0, 0]
            left_left_point_3 = [0, 0]
            right_right_point_3 = [0, 0]

            left_left_point[0] = left_point[0] - x_plus
            left_left_point[1] = left_point[1] - y_plus
            right_right_point[0] = right_point[0] + x_plus
            right_right_point[1] = right_point[1] + y_plus

            left_left_point_3[0] = left_left_point[0] - x_plus
            left_left_point_3[1] = left_left_point[1] - y_plus
            right_right_point_3[0] = right_right_point[0] + x_plus
            right_right_point_3[1] = right_right_point[1] + y_plus

            if self.the_color(chessboard, left_point, color)==COLOR_NONE and self.the_color(chessboard, right_point, color)==COLOR_NONE:
                if (self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==COLOR_NONE )or(self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==COLOR_NONE):
                    return 'jump_live_3'
                if (self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==color )or(self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==color):
                    return 'die_4'
                if (self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==-color )or(self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==-color):
                    return 'die_3'
                if (self.the_color(chessboard, right_right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point_3, color)==color )or(self.the_color(chessboard, left_left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point_3, color)==color):
                    return 'die_3'
                elif self.the_color(chessboard, left_left_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point, color)==COLOR_NONE:
                    return 'live_2'

            elif self.the_color(chessboard, left_point, color)==-color and self.the_color(chessboard, right_point, color)==-color:
                return 'nothing'

            elif self.the_color(chessboard, right_point, color)==COLOR_NONE or self.the_color(chessboard, left_point, color)==COLOR_NONE:
                if self.the_color(chessboard, right_point, color)==-color:
                    if self.the_color(chessboard, left_left_point, color)==-color or self.the_color(chessboard, left_left_point_3, color)==-color:
                        return 'nothing'
                    elif self.the_color(chessboard, left_left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point_3, color)==COLOR_NONE:
                        return 'die_2'
                    elif self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==color:
                        return 'die_4'
                    elif self.the_color(chessboard, left_left_point, color)==color or self.the_color(chessboard, left_left_point_3, color)==color:
                        return 'die_3'

                if self.the_color(chessboard, left_point, color)==-color:
                    if self.the_color(chessboard, right_right_point, color)==-color or self.the_color(chessboard, right_right_point_3, color)==-color:
                        return 'nothing'
                    elif self.the_color(chessboard, right_right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point_3, color)==COLOR_NONE:
                        return 'die_2'
                    elif self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==color:
                        return 'die_4'
                    elif self.the_color(chessboard, right_right_point, color)==color or self.the_color(chessboard, right_right_point_3, color)==color:
                        return 'die_3'

        elif cont ==1:
            left_left_point = [0, 0]
            right_right_point = [0, 0]
            left_left_point_3 = [0, 0]
            right_right_point_3 = [0, 0]
            left_left_point_4 = [0, 0]
            right_right_point_4 = [0, 0]

            left_left_point[0] = left_point[0] - x_plus
            left_left_point[1] = left_point[1] - y_plus
            right_right_point[0] = right_point[0] + x_plus
            right_right_point[1] = right_point[1] + y_plus

            left_left_point_3[0] = left_left_point[0] - x_plus
            left_left_point_3[1] = left_left_point[1] - y_plus
            right_right_point_3[0] = right_right_point[0] + x_plus
            right_right_point_3[1] = right_right_point[1] + y_plus

            left_left_point_4[0] = left_left_point_3[0] - x_plus
            left_left_point_4[1] = left_left_point_3[1] - y_plus
            right_right_point_4[0] = right_right_point_3[0] + x_plus
            right_right_point_4[1] = right_right_point_3[1] + y_plus
         #   print(right_point , right_right_point, right_right_point_3, right_right_point_4)

            if self.the_color(chessboard, left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==color and self.the_color(chessboard, left_left_point_4, color)==color :
                #print('l4')
                return 'low_die_4'
            if self.the_color(chessboard, right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==color and self.the_color(chessboard, right_right_point_4, color)==color :
               # print(self.the_color(chessboard, right_point, color), self.the_color(chessboard, right_right_point, color), self.the_color(chessboard, right_right_point_3, color), self.the_color(chessboard, right_right_point_4, color), color)
                return 'low_die_4'
            if self.the_color(chessboard, left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==color and self.the_color(chessboard, left_left_point_4, color)==COLOR_NONE and self.the_color(chessboard, right_point, color)==COLOR_NONE:
                return 'jump_live_3'
            if self.the_color(chessboard, right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==color and self.the_color(chessboard, right_right_point_4, color)==COLOR_NONE and self.the_color(chessboard, left_point, color)==COLOR_NONE :
                return 'jump_live_3'
            if self.the_color(chessboard, left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==color and self.the_color(chessboard, left_left_point_4, color)==-color and self.the_color(chessboard, right_point, color)==COLOR_NONE:
                return 'die_3'
            if self.the_color(chessboard, right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==color and self.the_color(chessboard, right_right_point_4, color)==-color and self.the_color(chessboard, left_point, color)==COLOR_NONE :
                return 'die_3'
            if self.the_color(chessboard, left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point_3, color)==color and self.the_color(chessboard, left_left_point_4, color)==color :
                return 'die_3'
            if self.the_color(chessboard, right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point_3, color)==color and self.the_color(chessboard, right_right_point_4, color)==color :
                return 'die_3'
            if self.the_color(chessboard, left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point, color)==color and self.the_color(chessboard, left_left_point_3, color)==COLOR_NONE and self.the_color(chessboard, left_left_point_4, color)==COLOR_NONE and self.the_color(chessboard, right_point, color)==COLOR_NONE:
                return 'low_live_2'
            if self.the_color(chessboard, right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point, color)==color and self.the_color(chessboard, right_right_point_3, color)==COLOR_NONE and self.the_color(chessboard, right_right_point_4, color)==COLOR_NONE and self.the_color(chessboard, left_point, color)==COLOR_NONE :
                return 'low_live_2'
            if self.the_color(chessboard, left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point, color)==COLOR_NONE and self.the_color(chessboard, left_left_point_3, color)==color and self.the_color(chessboard, left_left_point_4, color)==COLOR_NONE and self.the_color(chessboard, right_point, color)==COLOR_NONE:
                return 'low_live_2'
            if self.the_color(chessboard, right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point, color)==COLOR_NONE and self.the_color(chessboard, right_right_point_3, color)==color and self.the_color(chessboard, right_right_point_4, color)==COLOR_NONE and self.the_color(chessboard, left_point, color)==COLOR_NONE :
                return 'low_live_2'



        return 'nothing'

    def the_color(self, chessboard, point, color):
        if point[0]>=0 and point[0]<=14  and point[1]>=0 and point[1]<=14 :
            return chessboard[point[0], point[1]]
        else :
            return -color

    def the_max_grades(self, color, chessboard):

        thePoint=[0,0]
        max=0
        opmax=0
        for i in range(0 ,15):

            for j in range(0,15):

                if chessboard[i,j]==COLOR_NONE:
                    #print(i)


                    temp=self.count_the_total_grades( i, j, chessboard, color)

                   # printo(temp)
                    if temp>max :
                        max=temp
                      #  opmax=self.count_the_total_grades( i, j, chessboard, -color)

                        thePoint[0]=i
                        thePoint[1]=j
                   # elif temp==max:
                      #  if self.count_the_total_grades( i, j, chessboard, -color)>=opmax:
                       #     max = temp
                       #     opmax = self.count_the_total_grades(i, j, chessboard, -color)
                       #     thePoint[0] = i
                         #   thePoint[1] = j



        return max, thePoint

    def count_the_total_grades(self, x, y, chessboard,color):
        dic ={'win_5': 0, 'live_4':0, 'die_4':0, 'live_3':0, 'die_3':0, 'jump_live_3':0, 'live_2':0, 'die_2':0,
              'low_die_4':0, 'nothing':0, 'low_live_2':0}

        ver = self.count_grades(color, x, y, chessboard, 'vertical')

        cro = self.count_grades(color, x, y, chessboard, 'cross')

        rig = self.count_grades(color, x, y, chessboard, 'right')
        lef = self.count_grades( color, x, y, chessboard, 'left')
       # print(ver, end=' ')
       # print(cro, end=' ')
       # print(rig, end=' ')
       # print(lef, end=' ')
        dic[ver] = dic[ver] + 1
        dic[cro] = dic[cro] + 1
        dic[rig] = dic[rig] + 1
        dic[lef] = dic[lef] + 1
        thecount=0
        #print(dic)
        if dic['win_5']>=1:

            thecount+= 1000000
        if dic['live_4']>=1 or dic['die_4']>=2 or (dic['die_4']>=1 and dic['live_3']>=1) or (dic['die_4']>=1 and dic['jump_live_3']>=1):

            thecount+= 100000
        if dic['live_3']>=2 or (dic['live_3']>=1 and dic['jump_live_3']>=1) or dic['jump_live_3']>=2 :
            thecount+= 50000

        if dic['die_4'] >= 1:
            thecount += 10000

        if dic['low_die_4'] >= 1:
            thecount += 9000
        if dic['live_3']>=1 and dic['live_3']>=1:
            thecount+= 7000
        if dic['live_3']>=1 and dic['die_3']>=1:
            thecount+= 5000
        if dic['live_3']>=1:
            thecount+= 1000
        if dic['jump_live_3']>=1:
            thecount+= 900
        if dic['live_2']>=2:
            thecount+= 500
        if dic['live_2']>=1:
            thecount+= 100
        if dic['low_live_2']>=1:
            thecount+= 90
        if dic['die_3']>=1:
            thecount+= 50
        if dic['die_2']>=1:
            thecount+= 20
        thecount+=dic['nothing']

        return thecount




