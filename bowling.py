class Bowling:

    def __init__(self) -> None:
        self.score_table = []
        self.total_score = 0

    def add_points(self, first_ball, second_ball=0):
        self.score_table.append([first_ball, second_ball])

    def calculate_point(self):
        for index, points in enumerate(self.score_table):
            self.total_score += sum(points)
        return self.total_score

    def show_score_table(self):
        print(self.score_table)


player1 = Bowling()
player1.add_points(1,2)
player1.add_points(8,2)
player1.add_points(7,1)
player1.add_points(10)
player1.add_points(5,3)
player1.show_score_table()
print(player1.calculate_point())

