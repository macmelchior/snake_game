from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.color('gray')
        self.speed('fastest')
        self.new_location()

    def new_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
