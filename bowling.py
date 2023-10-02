class Bowling:

    def __init__(self) -> None:
        self.frame_table = []
        self.score_table = []

    def add_points(self, first_ball, second_ball=0):
        self.frame_table.append([first_ball, second_ball])

    #This function will calculate ALL scores 
    def full_calculate_point(self):
        
        self.score_table.clear() #ERASE all the calculated points and start from zero

        for frame, points in enumerate(self.frame_table):
        
            #STRIKE
            if points[0] == 10:
                self.score_table.append(None)

                #Check if it is a TRIPLE STRIKE
                if frame >=2: #It is possible only after the 3 frame
                    if (self.frame_table[frame-1][0] == 10) and (self.frame_table[frame-2][0] == 10): #it is waiting extra points
                        self.score_table[frame-2] = 30

                #Check if previous frame is waiting for extra points
                if frame >=1: #You can NOT check the last frame if it is the Fisrt frame
                    if self.score_table[frame-1] is None:
                        
                        if self.frame_table[frame-1][0] == 10: #check if the last frame was a Strike
                            pass
                        else:
                            self.score_table[frame-1] = 20


            #SPERE
            elif sum(points) == 10:
                self.score_table.append(None)

                #Check if previous frame is waiting for extra points
                if frame >=1: #You can NOT check the last frame if it is the Fisrt frame
                    if self.score_table[frame-1] is None:
                        
                        if self.frame_table[frame-1][0] == 10: #check if the last frame was a Strike
                            self.score_table[frame-1] = 20
                        else:
                            self.score_table[frame-1] = 10 + points[0]


            #NORMAL frame - No strike and NO spere
            else:
                self.score_table.append(sum(points))

                #Check if previous frame is waiting for extra points
                if frame >=1: #You can NOT check the last frame if it is the Fisrt frame
                    
                    if self.score_table[frame-1] is None: #it is waiting extra points
                        
                        if self.frame_table[frame-1][0] == 10: #check if the last frame was a Strike
                            self.score_table[frame-1] = 10 + sum(points)
                        else:
                            self.score_table[frame-1] = 10 + points[0]
                        
                        #Check if 2 frames ago is waiting for extra points - Duble Strike
                        if frame >=2: #It is possible only after the 3 frame
                            if self.score_table[frame-2] is None:
                                self.score_table[frame-2] = 10 + 10 + points[0]
                                    

        return True


    #This function calculates the score only for the new Frame add (last one).
    def calculate_frame_point(self):
          
        frame = len(self.frame_table)-1
        points = self.frame_table[frame]

        #STRIKE
        if points[0] == 10:
            self.score_table.append(None)

            #Check if it is a TRIPLE STRIKE
            if frame >=2: #It is possible only after the 3 frame
                if (self.frame_table[frame-1][0] == 10) and (self.frame_table[frame-2][0] == 10): #it is waiting extra points
                    self.score_table[frame-2] = 30

            #Check if previous frame is waiting for extra points
            if frame >=1: #You can NOT check the last frame if it is the Fisrt frame
                if self.score_table[frame-1] is None:
                    
                    if self.frame_table[frame-1][0] == 10: #check if the last frame was a Strike
                        pass
                    else:
                        self.score_table[frame-1] = 20


        #SPERE
        elif sum(points) == 10:
            self.score_table.append(None)

            #Check if previous frame is waiting for extra points
            if frame >=1: #You can NOT check the last frame if it is the Fisrt frame
                if self.score_table[frame-1] is None:
                    
                    if self.frame_table[frame-1][0] == 10: #check if the last frame was a Strike
                        self.score_table[frame-1] = 20
                    else:
                        self.score_table[frame-1] = 10 + points[0]


        #NORMAL frame - No strike and NO spere
        else:
            self.score_table.append(sum(points))

            #Check if previous frame is waiting for extra points
            if frame >=1: #You can NOT check the last frame if it is the Fisrt frame
                
                if self.score_table[frame-1] is None: #it is waiting extra points
                    
                    if self.frame_table[frame-1][0] == 10: #check if the last frame was a Strike
                        self.score_table[frame-1] = 10 + sum(points)
                    else:
                        self.score_table[frame-1] = 10 + points[0]
                    
                    #Check if 2 frames ago is waiting for extra points - Duble Strike
                    if frame >=2: #It is possible only after the 3 frame
                        if self.score_table[frame-2] is None:
                            self.score_table[frame-2] = 10 + 10 + points[0]
                                    

        return True
    #===============

    def show_frame_table(self):
        print(self.frame_table)
    
    def show_score_table(self):
        print(self.score_table)

    def show_total_score(self):
        soma = sum((x for x in self.score_table if x is not None))
        print(soma)


player1 = Bowling()
player1.add_points(8,2)
player1.calculate_frame_point()
player1.add_points(5,4)
player1.calculate_frame_point()
player1.add_points(10,0)
player1.calculate_frame_point()
player1.add_points(2,1)
player1.calculate_frame_point()

player1.show_frame_table()
player1.show_score_table()
player1.show_total_score()

player1.full_calculate_point()
player1.show_score_table()
player1.show_total_score()



