from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.hideturtle()
        self.color('white')
        self.show_score()

    def show_score(self):
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over.', align=ALIGN, font=FONT)
