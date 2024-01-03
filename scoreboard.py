from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 32, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score_1 = 0
        self.current_score_2 = 0
        self.penup()
        # self.write_dotted_line()
        self.hideturtle()
        self.goto(0, 200)
        self.color("white")
        self.write(f"Score:\n{self.current_score_1}:{self.current_score_2}", move=False, align=ALIGNMENT, font=FONT)

    def write_dotted_line(self):
        self.penup()
        self.goto(0, -300)
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def add_score_1(self):
        self.current_score_1 += 1
        self.change_score()

    def add_score_2(self):
        self.current_score_2 += 1
        self.change_score()

    def change_score(self):
        self.clear()
        self.write(f"Score: \n{self.current_score_1}:{self.current_score_2}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.write(f"Game over.", move=False, align=ALIGNMENT, font=FONT)
