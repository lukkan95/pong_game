from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 32, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score_1 = 0
        self.current_score_2 = 0
        self.create_description()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.write_dotted_line()
        self.goto(0, 210)
        self.write(f"{self.current_score_1}:{self.current_score_2}", move=False, align=ALIGNMENT, font=FONT)

    def create_description(self):
        description = self
        description.penup()
        description.color("white")
        description.speed("fastest")
        description.hideturtle()
        description.goto(0, 250)
        description.write(f"Score", move=False, align=ALIGNMENT, font=FONT)

    def write_dotted_line(self):
        self.goto(0, -300)
        self.left(90)
        for i in range(26):
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
        self.write(f"{self.current_score_1}:{self.current_score_2}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.write(f"Game over.", move=False, align=ALIGNMENT, font=FONT)
