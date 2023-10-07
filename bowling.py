class Bowling:

    def __init__(self) -> None:
        self.frame_table = []
        self.score_table = []

    def add_points(self, first_ball, second_ball=0, extra_ball_frame10=0):
        if len(self.frame_table) == 9:
            self.frame_table.append([first_ball, second_ball, extra_ball_frame10])
        else:
            self.frame_table.append([first_ball, second_ball])

    
    def calculate_points(self, full=False):

        if full == True:
            self.score_table.clear()
            for frame, points in enumerate(self.frame_table):
                self.calculate_single_frame_point(frame, points)

        else:
            frame = len(self.frame_table)-1
            points = self.frame_table[frame]
            self.calculate_single_frame_point(frame,points)


    def calculate_single_frame_point(self, frame, points):
          
        #STRIKE
        if points[0] == 10:
            self.score_table.append(None)
        
        #SPARE
        elif points[0] + points[1] == 10:
            self.score_table.append(None)

        #NORMAL frame - No strike and No spare
        else:
            self.score_table.append(points[0] + points[1])
        
        #For the Frame 10 - END Frame - No more balls
        if frame == 9:
            self.score_table[9] = sum(points)
        

        #Check if previous frame is waiting for extra points
        if frame >=1: #You can NOT check the last frame IF it is the Fisrt frame
            if self.score_table[frame-1] is None:
                
                #Last frame is Strike (x)
                if self.frame_table[frame-1][0] == 10: 
                    
                    #Actual Frame is also Strike
                    if points[0] == 10: 
                        
                        #Check if it is a TRIPLE STRIKE - (x)(x)(x)
                        if frame>=2:  #It is possible only after the 3 frame
                            if self.score_table[frame-2] is None:
                                self.score_table[frame-2] = 30
                        
                        #It is only Duble Strike - (x)(x)
                        if frame == 9: #Exception - LAST Frame
                            self.score_table[frame-1] = 20 + points[1]
                            
                        #It continue to be None - (none)(none)
                        else:
                            pass 

                    #Actual frame is a Normal frame or Spare (x)(9,1)
                    else:
                        self.score_table[frame-1] = 10 + points[0] + points[1]

                #Last frame is Spare
                else:
                        self.score_table[frame-1] = 10 + points[0]


    def show_frame_table(self):
        print(self.frame_table)
    
    def show_score_table(self):
        print(self.score_table)

    def show_total_score(self):
        soma = sum((x for x in self.score_table if x is not None))
        print(soma)



#===== Testing cases=====

player1 = Bowling()

player1.add_points(8,2)
player1.calculate_points()
player1.add_points(5,4)
player1.calculate_points()
player1.add_points(10,0)
player1.calculate_points()
player1.add_points(2,1)
player1.calculate_points()
player1.add_points(2,1)
player1.calculate_points()
player1.add_points(2,1)
player1.calculate_points()
player1.add_points(2,1)
player1.calculate_points()
player1.add_points(2,1,3)
player1.calculate_points()
player1.add_points(10)
player1.calculate_points()
player1.add_points(10,10,5)
player1.calculate_points()

player1.show_frame_table()
player1.show_score_table()
player1.show_total_score()


player1.calculate_points(True)
player1.show_score_table()
player1.show_total_score()
print(player1.score_table[1])



